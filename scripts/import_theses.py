"""导入 reference/ 下的中文学位论文到 Zotero（通过 connector API）"""
import json
import urllib.request
import time

API_CONNECTOR = "http://localhost:23119/connector/saveItems"
API_LOCAL = "http://localhost:23119/api/users/0"

# 学位论文元数据
theses = [
    {
        "title": "移动扩频水声通信及多址技术研究",
        "creators": [{"firstName": "", "lastName": "杜鹏宇", "creatorType": "author"}],
        "university": "哈尔滨工程大学",
        "thesisType": "博士学位论文",
        "date": "2019",
        "tags": ["扩频", "DSSS", "水声通信"],
        "pdf": r"D:\Claude\TechReq\UWAcomm\reference\移动扩频水声通信及多址技术研究_杜鹏宇.pdf",
    },
    {
        "title": "强干扰环境下单载波水声通信技术研究",
        "creators": [{"firstName": "", "lastName": "未知", "creatorType": "author"}],
        "university": "哈尔滨工程大学",
        "thesisType": "学位论文",
        "date": "",
        "tags": ["单载波", "水声通信", "干扰"],
        "pdf": r"D:\Claude\TechReq\UWAcomm\reference\强干扰环境下单载波水声通信技术研究.pdf",
    },
    {
        "title": "快时变信道下的水声通信技术研究",
        "creators": [{"firstName": "", "lastName": "未知", "creatorType": "author"}],
        "university": "哈尔滨工程大学",
        "thesisType": "学位论文",
        "date": "",
        "tags": ["时变信道", "水声通信"],
        "pdf": r"D:\Claude\TechReq\UWAcomm\reference\快时变信道下的水声通信技术研究.pdf",
    },
    {
        "title": "水声MIMO信道容量和系统实现关键技术研究",
        "creators": [{"firstName": "", "lastName": "未知", "creatorType": "author"}],
        "university": "哈尔滨工程大学",
        "thesisType": "学位论文",
        "date": "",
        "tags": ["MIMO", "水声通信"],
        "pdf": r"D:\Claude\TechReq\UWAcomm\reference\水声MIMO信道容量和系统实现关键技术研究.pdf",
    },
    {
        "title": "浅海环境下单载波时域均衡水声通信关键技术研究",
        "creators": [{"firstName": "", "lastName": "未知", "creatorType": "author"}],
        "university": "哈尔滨工程大学",
        "thesisType": "学位论文",
        "date": "",
        "tags": ["单载波", "时域均衡", "水声通信"],
        "pdf": r"D:\Claude\TechReq\UWAcomm\reference\浅海环境下单载波时域均衡水声通信关键技术研究.pdf",
    },
]


def save_item(thesis):
    """通过 connector API 保存条目"""
    item = {
        "itemType": "thesis",
        "title": thesis["title"],
        "creators": thesis["creators"],
        "university": thesis["university"],
        "thesisType": thesis["thesisType"],
        "date": thesis["date"],
        "tags": thesis["tags"],
        "attachments": [
            {
                "url": "file:///" + thesis["pdf"].replace("\\", "/"),
                "title": thesis["pdf"].split("\\")[-1],
                "mimeType": "application/pdf",
            }
        ],
    }

    payload = json.dumps(
        {"items": [item], "uri": "http://localhost", "sessionID": f"import_{hash(thesis['title'])}"}
    ).encode("utf-8")

    req = urllib.request.Request(API_CONNECTOR, data=payload, method="POST")
    req.add_header("Content-Type", "application/json")

    try:
        with urllib.request.urlopen(req) as resp:
            print(f"  OK (status {resp.status})")
            return True
    except Exception as e:
        msg = e.read().decode("utf-8")[:200] if hasattr(e, "read") else str(e)
        print(f"  FAILED: {msg}")
        return False


def add_to_collection(item_key, collection_key):
    """将条目添加到 collection（通过修改 collections 字段）"""
    # 读取当前条目
    url = f"{API_LOCAL}/items/{item_key}"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as resp:
        item = json.loads(resp.read().decode("utf-8"))

    current_collections = item["data"].get("collections", [])
    if collection_key not in current_collections:
        current_collections.append(collection_key)

    # 通过 PATCH 更新（如果API支持）
    patch_data = json.dumps({"collections": current_collections}).encode("utf-8")
    req = urllib.request.Request(url, data=patch_data, method="PATCH")
    req.add_header("Content-Type", "application/json")
    req.add_header("If-Unmodified-Since-Version", str(item["version"]))
    try:
        with urllib.request.urlopen(req) as resp:
            print(f"  Added to collection {collection_key}")
            return True
    except Exception as e:
        print(f"  Collection assignment skipped (API limitation)")
        return False


if __name__ == "__main__":
    print("Importing theses to Zotero...")
    print()

    for t in theses:
        print(f"Importing: {t['title']}")
        save_item(t)
        time.sleep(0.5)
        print()

    print("Done! Please assign to collections manually in Zotero if needed.")
