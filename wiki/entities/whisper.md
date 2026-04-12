---
type: entity
created: 2026-04-12
updated: 2026-04-12
tags: [工具, 视频转录, 语音识别]
entity_type: tool
---

# Whisper

OpenAI 开源的语音识别模型，是 my-brain 系统中**本地视频转录工具**。

## 角色定位

完全本地运行，不上传内容，支持中文，准确率高。适合处理本地录像、会议录屏、课程视频、无字幕视频以及内容敏感不想上云的资料。

## 基本用法

```bash
pip install openai-whisper
whisper video.mp4 --language Chinese --output_format txt --output_dir raw/videos/
```

转录后建议交给 [[claude-code]] 做结构化处理（加标题和段落分隔），再存入 `raw/videos/`。

## 适用场景

| 场景 | 是否适用 |
|------|----------|
| 本地视频，内容敏感 | 最佳选择 |
| YouTube 视频 | 建议用 [[firecrawl]] |
| 偶发需求，快速处理 | 建议用 VOMO AI |

## 来源

- [[toolchain.md|工具链指南]] — 描述了 Whisper 的角色和使用方式
