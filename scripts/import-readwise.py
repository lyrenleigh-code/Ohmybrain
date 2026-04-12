#!/usr/bin/env python3
"""
Readwise 文章导入脚本：扫描 Readwise 导出目录，将 markdown 文件复制到 raw/articles/。
用法：
  python3 scripts/import-readwise.py <导出目录>

Readwise Reader 导出设置：
  格式选 Markdown，导出到本地文件夹后运行此脚本。
"""
import sys
import os
import io
import shutil
import argparse
from datetime import date

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

OUTPUT_DIR = "raw/articles"


def import_articles(source_dir):
    if not os.path.exists(source_dir):
        print(f"错误：���录不存在 — {source_dir}")
        sys.exit(1)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    today = date.today().isoformat()

    imported = 0
    skipped = 0
    for f in os.listdir(source_dir):
        if not f.endswith(".md"):
            continue

        source_path = os.path.join(source_dir, f)
        # 如果文件名没有日期前缀，加上
        if not f[:4].isdigit():
            target_name = f"{today}-{f}"
        else:
            target_name = f

        target_path = os.path.join(OUTPUT_DIR, target_name)
        if os.path.exists(target_path):
            skipped += 1
            continue

        shutil.copy2(source_path, target_path)
        imported += 1

    print(f"导入完成：{imported} 篇新文章，{skipped} 篇已存在跳过")
    if imported > 0:
        print(f"下一步：对新文章执行 /ingest-source")


def main():
    parser = argparse.ArgumentParser(description="Readwise 文章导入")
    parser.add_argument("source", help="Readwise 导出目录路径")
    args = parser.parse_args()
    import_articles(args.source)


if __name__ == "__main__":
    main()
