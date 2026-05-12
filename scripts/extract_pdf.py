#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Extract text from PDFs using PyMuPDF.

Usage:
    python extract_pdf.py <path> [--pages START-END]
    python extract_pdf.py --batch <batch-name>

Batches are predefined groups of UWAnet PDFs for bulk ingest.
"""
import argparse
import io
import sys
from pathlib import Path

import fitz  # PyMuPDF

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

UWANET_RAW = Path("D:/Claude/TechReq/UWAnet/raw")

BATCHES = {
    "uwanet-install": [
        ("courses/NS3资料/NS3安装教程/基于 WSL2 的 NS3 环境搭建教程_wsl 支持 ns3 吗 - CSDN 博客.pdf", 0, 10),
        ("courses/NS3资料/NS3安装教程/在 Win11 安装 Ubuntu20_04 子系统 WSL2 到其他盘（此处为 D 盘，因为 C 盘空间实在不能放应用）_wsl2 安装 ubantu 到 d 盘 - CSDN 博客.pdf", 0, 10),
        ("courses/NS3资料/NS3安装教程/【ns-3】VS Code 开发环境配置_如何用 vscode 打开 ns3-CSDN 博客.pdf", 0, 10),
        ("courses/NS3资料/NS3官方文档/ns-3-installation.pdf", 0, 15),
    ],
    "uwanet-papers": [
        ("papers/Aqua-Net_An_underwater_sensor_network_architecture_Design_implementation_and_initial_testing.pdf", 0, 20),
        ("papers/Aqua-Sim_Fourth_Generation_Towards_General_and_Intelligent_Simulation_for_Underwater_Acoustic_Networks.pdf", 0, 20),
        ("papers/Molins+和+Stojanovic+-+2006+-+Slotted+FAMA+a+MAC+protocol+for+underwater+acoust.pdf", 0, 15),
        ("papers/Potter+等+-+2014+-+The+JANUS+underwater+communications+standard.pdf", 0, 15),
    ],
    "uwanet-nsofficial": [
        ("courses/NS3资料/NS3官方文档/ns-3-manual.pdf", 0, 5),
        ("courses/NS3资料/NS3官方文档/ns-3-tutorial-3.40.pdf", 0, 5),
        ("courses/NS3资料/NS3官方文档/ns-3-model-library.pdf", 0, 5),
    ],
}


def extract_one(path: Path, start: int, end: int) -> None:
    if not path.exists():
        print(f"!!! MISSING: {path}")
        return
    try:
        doc = fitz.open(str(path))
        n = len(doc)
        print(f"=== {path.name} (total {n} pages, extracting {start + 1}..{min(end, n)}) ===")
        for i in range(start, min(end, n)):
            text = doc[i].get_text()
            if text.strip():
                print(f"--- page {i + 1} ---")
                print(text)
        doc.close()
    except Exception as e:
        print(f"!!! ERROR on {path}: {e}")


def run_batch(name: str, base: Path) -> None:
    for rel, start, end in BATCHES[name]:
        extract_one(base / rel, start, end)
    print("=== BATCH DONE ===")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", help="PDF file path")
    parser.add_argument("--pages", help="page range, e.g. 1-10")
    parser.add_argument("--batch", choices=list(BATCHES.keys()))
    args = parser.parse_args()

    if args.batch:
        run_batch(args.batch, UWANET_RAW)
        return 0

    if not args.path:
        parser.print_help()
        return 1

    start, end = 0, 1_000_000
    if args.pages:
        s, e = args.pages.split("-")
        start, end = int(s) - 1, int(e)
    extract_one(Path(args.path), start, end)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
