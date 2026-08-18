#!/usr/bin/env python
"""backup_push.py — 本地单点仓的双轨备份（2026-08-18 审计十五第 3 项落地）。

背景：DigitalTwin1plusN 教训——本地 git 无远程，目录一删 12 commit 历史全没。
本脚本对工作区全仓（复用 dashboard_snapshot.discover_repos 自动发现）提供两轨：

  python scripts/backup_push.py --bundle        # 离线轨：git bundle 到 Archive/git-backups/
  python scripts/backup_push.py --push          # 在线轨：内网 gitlab 可达时批量 push
  python scripts/backup_push.py --push --dry    # 只列会 push 什么，不动

--bundle：对「无远程」或「领先远程」的仓生成带日期 bundle（含全部 refs），
  同名当日文件覆盖（一天多跑不堆积）；跨日保留历史快照，人工按需清理。
--push：先探测 gitlab 连通性（不可达则整体跳过 exit 0）；对已配 gitlab remote 的仓
  push 当前分支（首推 -u；push-to-create 依赖 GitLab 命名空间权限，失败逐仓报告
  不中断）。Ohmybrain 本仓默认跳过（push 节奏由用户在 Hub 会话单独授权）。

注意：本脚本**不做任何 commit**——工作树未提交内容不属于备份轨，归各项目业务面。
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
# UTF-8 stdout 包裹由 dashboard_snapshot 模块级代码完成（import 即生效）；
# 此处不得重复包裹——两层 TextIOWrapper 叠同一 buffer，弃置层 GC 时会连底层一起关闭。
from dashboard_snapshot import _git, discover_repos, find_hub_root  # noqa: E402

GITLAB_PROBE = "http://192.168.10.100:8880/lilin/Ohmybrain.git"
# push 轨默认不碰的仓：Hub 自身（push 由用户单独授权）+ 敏感/未登记仓
PUSH_SKIP = {"Ohmybrain", "Patents", "DocProcess/papers",
             "Tools/MetalDinoForge", "Tools/ObsidianStyleLab", "Tools/SlotForge",
             "Tools/ppt-master"}


def repo_state(repo: Path) -> tuple[str, str, list[str], int]:
    """(branch, head-hash, remotes, ahead-of-first-remote)。无 commit → head 空。"""
    branch = _git(repo, "rev-parse", "--abbrev-ref", "HEAD") or "?"
    head = _git(repo, "rev-parse", "--short", "HEAD")
    remotes = _git(repo, "remote").splitlines()
    ahead = 0
    if head and remotes:
        n = _git(repo, "rev-list", "--count", f"{remotes[0]}/{branch}..HEAD")
        ahead = int(n) if n.isdigit() else 0
    return branch, head, remotes, ahead


def do_bundle(workspace: Path) -> int:
    out = workspace / "Archive" / "git-backups"
    out.mkdir(parents=True, exist_ok=True)
    stamp = date.today().strftime("%Y%m%d")
    made = skipped = 0
    for label, repo in discover_repos(workspace):
        if not _git(repo, "rev-parse", "--git-dir"):
            continue
        branch, head, remotes, ahead = repo_state(repo)
        if not head:
            print(f"  - {label}: 0 commit，跳过（先入库才有可备份历史）")
            continue
        # 已有远程、远程分支真实存在、且未领先 = 远程即备份，跳过。
        # 注意：仅「配了 remote 但从未 push」（远程 ref 不存在）不算已备份。
        remote_ref_ok = bool(remotes) and bool(
            _git(repo, "rev-parse", "--verify", "--quiet", f"{remotes[0]}/{branch}"))
        if remote_ref_ok and ahead == 0:
            skipped += 1
            continue
        target = out / f"{Path(label).name}-{stamp}.bundle"
        try:
            r = subprocess.run(
                ["git", "-C", str(repo), "bundle", "create", str(target), "--all"],
                capture_output=True, text=True, timeout=300)
            ok = r.returncode == 0
        except (OSError, subprocess.TimeoutExpired):
            ok = False
        print(f"  {'✓' if ok else '✗'} {label} → {target.name}")
        made += ok
    print(f"[bundle] {made} 个已生成，{skipped} 个已有同步远程跳过 → {out}")
    return 0


def do_push(workspace: Path, dry: bool) -> int:
    if not _git(workspace / "Ohmybrain", "ls-remote", GITLAB_PROBE, "HEAD"):
        print("[push] 内网 gitlab 不可达（不在内网？），本轮跳过。")
        return 0
    pushed = failed = 0
    for label, repo in discover_repos(workspace):
        if label in PUSH_SKIP or not _git(repo, "rev-parse", "--git-dir"):
            continue
        branch, head, remotes, ahead = repo_state(repo)
        if not head or "gitlab" not in remotes:
            continue
        tracked = _git(repo, "rev-parse", "--abbrev-ref", f"{branch}@{{upstream}}")
        if tracked and ahead == 0:
            continue
        if dry:
            print(f"  [dry] {label}: 将 push {branch}（{'首推' if not tracked else f'领先 {ahead}'}）")
            continue
        try:
            r = subprocess.run(
                ["git", "-C", str(repo), "push", "-u", "gitlab", branch],
                capture_output=True, text=True, timeout=300)
            ok = r.returncode == 0
        except (OSError, subprocess.TimeoutExpired):
            ok = False
        print(f"  {'✓' if ok else '✗'} {label} push {branch}"
              + ("" if ok else f"（{(r.stderr or '').strip().splitlines()[-1] if r.stderr else '超时/异常'}）"))
        pushed += ok
        failed += (not ok)
    print(f"[push] ✓{pushed} ✗{failed}；完成后可跑 dashboard_snapshot.py --gen 刷新快照")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="本地单点仓双轨备份（bundle / push）")
    ap.add_argument("--bundle", action="store_true", help="离线轨：git bundle 到 Archive/git-backups/")
    ap.add_argument("--push", action="store_true", help="在线轨：内网 gitlab 批量 push")
    ap.add_argument("--dry", action="store_true", help="--push 时只列计划不执行")
    args = ap.parse_args()
    hub = find_hub_root(Path(__file__).resolve().parent)
    if hub is None:
        print("ERROR: 未找到 Hub 根", file=sys.stderr)
        return 1
    ws = hub.parent
    if args.bundle:
        return do_bundle(ws)
    if args.push:
        return do_push(ws, args.dry)
    ap.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
