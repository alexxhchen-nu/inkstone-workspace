---
title: Start Here
aliases:
  - 从这里开始
tags:
  - start
---

# Start Here

这是 Untangle 考古笔记的 Obsidian 起始库（简体中文）。用「打开文件夹作为库」打开本文件夹即可，不要嵌进别的库。

## 下一步

1. 把考古报告（PDF、Word、图片，或已有的 Markdown）放进 [[Inbox]]。
2. 在文件上右键，选 **Parse to Markdown**（Archaeo Doc Parser）。结果写到 [[Parsed]]。免费档不用填 MinerU token。
3. 打开生成的 Markdown，命令面板运行 **Parse archaeological tombs**（Archaeological Tomb Parser）。结果写到 [[Tombs]]，在源文件名下再建一个 `*_tombs` 子文件夹。
4. 用模板补笔记：[[Templates/Site|遗址]]、[[Templates/Tomb|墓葬]]、[[Templates/Artifact|器物]]、[[Templates/Report|报告]]。通用笔记用 [[Templates/New Note|新笔记]]。

更短的步骤见 [[快速上手]]。插件安装和「为什么要装」见 [[README]]。

## 文件夹

| 文件夹 | 用来放什么 |
| --- | --- |
| Inbox | 报告原文（PDF、Office、图片或 Markdown） |
| Parsed | 文档解析得到的 Markdown |
| Tombs | 抽取后的墓葬数据 |
| Sites | 遗址笔记 |
| Artifacts | 器物笔记 |
| Attachments | 图片和附件 |
| Templates | 配套模板 |

## 示例

库里有一份合成示例：[[Inbox/示例墓葬文本]]。打开它，运行 **Parse archaeological tombs**，应能抽出 M1（土坑竖穴墓，墓口长 2.5 米、宽 1.2 米、深 3.0 米）。这不是真实发掘报告，只用来试命令。
