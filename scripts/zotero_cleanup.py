#!/usr/bin/env python3
"""
Zotero 重复条目清理脚本。
将重复条目移入 Zotero 回收站（可在 Zotero 中恢复）。

重要：运行前请先关闭 Zotero！

策略：
- 通用/垃圾标题（IEEE Xplore Full Text PDF 等）→ 全部移入回收站
- 真实重复论文 → 保留有文件夹归类的最早条目，其余移入回收站

用法：
  python3 scripts/zotero_cleanup.py --dry-run   # 仅预览，不修改
  python3 scripts/zotero_cleanup.py --execute    # 执行清理
"""
import sqlite3, os, io, sys, re, json
from collections import defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

GENERIC_TITLES = [
    'ieee xplore full text pdf', 'full text pdf', 'snapshot',
    'ieee xplore abstract record', 'ieee xplore full-text pdf',
]

def normalize(t):
    t = t.lower().strip()
    t = re.sub(r'[^\w\s]', '', t)
    t = re.sub(r'\s+', ' ', t)
    return t

def scan(conn):
    c = conn.cursor()
    c.execute("""
        SELECT i.itemID, idv.value as title, i.dateAdded,
               (SELECT GROUP_CONCAT(c.collectionName, '; ')
                FROM collectionItems ci JOIN collections c ON ci.collectionID=c.collectionID
                WHERE ci.itemID=i.itemID) as collections
        FROM items i
        JOIN itemData id ON i.itemID=id.itemID
        JOIN itemDataValues idv ON id.valueID=idv.valueID
        JOIN fields f ON id.fieldID=f.fieldID
        WHERE f.fieldName='title'
          AND i.itemTypeID NOT IN (14, 1)
          AND i.itemID NOT IN (SELECT itemID FROM deletedItems)
        ORDER BY idv.value
    """)
    rows = c.fetchall()

    groups = defaultdict(list)
    for itemID, title, dateAdded, colls in rows:
        key = normalize(title)
        if len(key) > 3:
            groups[key].append((itemID, title, dateAdded, colls))

    to_trash = []

    for key, items in groups.items():
        if key in GENERIC_TITLES:
            to_trash.extend([it[0] for it in items])
        elif len(items) > 1:
            scored = []
            for itemID, title, dateAdded, colls in items:
                has_colls = 1 if colls else 0
                scored.append((has_colls, dateAdded, itemID))
            scored.sort(key=lambda x: (-x[0], x[1]))
            to_trash.extend([s[2] for s in scored[1:]])

    return to_trash, len(rows)

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ('--dry-run', '--execute'):
        print("用法: python3 scripts/zotero_cleanup.py [--dry-run|--execute]")
        sys.exit(1)

    dry_run = sys.argv[1] == '--dry-run'
    db = os.path.expanduser("~/Zotero/zotero.sqlite")

    if not os.path.exists(db):
        print(f"错误：数据库不存在 — {db}")
        sys.exit(1)

    conn = sqlite3.connect(db)
    to_trash, total = scan(conn)

    print(f"总条目数: {total}")
    print(f"待清理条目: {len(to_trash)}")
    print(f"清理后剩余: {total - len(to_trash)}")
    print()

    if dry_run:
        print("[预览模式] 不会修改数据库")
        print(f"将有 {len(to_trash)} 条被移入回收站")
    else:
        print("[执行模式] 正在移入回收站...")
        c = conn.cursor()
        for item_id in to_trash:
            c.execute("INSERT OR IGNORE INTO deletedItems (itemID) VALUES (?)", (item_id,))
        conn.commit()
        print(f"已将 {len(to_trash)} 条移入回收站")
        print("请打开 Zotero 检查回收站，确认无误后可清空回收站")

    conn.close()

if __name__ == "__main__":
    main()
