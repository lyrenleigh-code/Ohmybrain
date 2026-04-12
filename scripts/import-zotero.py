#!/usr/bin/env python3
"""
Zotero 论文导入脚本：扫描 Zotero 存储目录，将 PDF 和 metadata 复制到 raw/papers/。
用法：
  python3 scripts/import-zotero.py [--zotero-dir PATH]

默认 Zotero 存储目录：
  Windows: C:/Users/<user>/Zotero/storage/
  macOS:   ~/Zotero/storage/
"""
import sys
import os
import io
import shutil
import argparse
from datetime import date

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

DEFAULT_ZOTERO_DIR = os.path.expanduser("~/Zotero/storage")
OUTPUT_DIR = "raw/papers"


def find_pdfs(zotero_dir):
    """递归查找 Zotero storage 下所有 PDF 文件"""
    pdfs = []
    for root, _, files in os.walk(zotero_dir):
        for f in files:
            if f.lower().endswith(".pdf"):
                pdfs.append(os.path.join(root, f))
    return pdfs


def import_papers(zotero_dir):
    if not os.path.exists(zotero_dir):
        print(f"错误：Zotero 目录不存在 — {zotero_dir}")
        sys.exit(1)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    pdfs = find_pdfs(zotero_dir)
    today = date.today().isoformat()

    if not pdfs:
        print("未找到 PDF 文件")
        return

    imported = 0
    skipped = 0
    for pdf_path in pdfs:
        filename = os.path.basename(pdf_path)
        target = os.path.join(OUTPUT_DIR, filename)

        if os.path.exists(target):
            skipped += 1
            continue

        shutil.copy2(pdf_path, target)
        imported += 1

        # 生成配套的 metadata markdown
        name_no_ext = os.path.splitext(filename)[0]
        md_path = os.path.join(OUTPUT_DIR, f"{today}-{name_no_ext}.md")
        if not os.path.exists(md_path):
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(f"""# {name_no_ext}

- **来源**：Zotero
- **日期**：{today}
- **类型**：论文
- **PDF**：{filename}

## 关键内容

（待 ingest 时由 Claude Code 填充）
""")

    print(f"导入完成：{imported} 篇新论文，{skipped} 篇已存在跳过")
    if imported > 0:
        print(f"下一步：对新论���执行 /ingest-source")


def main():
    parser = argparse.ArgumentParser(description="Zotero 论文导入")
    parser.add_argument("--zotero-dir", default=DEFAULT_ZOTERO_DIR,
                        help=f"Zotero storage 目录（默认 {DEFAULT_ZOTERO_DIR}）")
    args = parser.parse_args()
    import_papers(args.zotero_dir)


if __name__ == "__main__":
    main()
