---
title: Start Here
aliases:
  - 從這裡開始
tags:
  - start
---

# Start Here

這是 Untangle 考古筆記的 Obsidian 起始庫（繁體中文）。用「開啟資料夾作為儲存庫」開啟本資料夾即可，不要嵌進別的庫。

## 下一步

1. 把考古報告（PDF、Word、圖片，或既有的 Markdown）放進 [[Inbox]]。
2. 在檔案上按右鍵，選 **Parse to Markdown**（Archaeo Doc Parser）。結果會寫到 [[Parsed]]。免費方案不必填 MinerU token。
3. 開啟產生的 Markdown，命令面板執行 **Parse archaeological tombs**（Archaeological Tomb Parser）。結果會寫到 [[Tombs]]，在來源檔名下再建立一個 `*_tombs` 子資料夾。
4. 用範本補筆記：[[Templates/Site|遺址]]、[[Templates/Tomb|墓葬]]、[[Templates/Artifact|器物]]、[[Templates/Report|報告]]。通用筆記用 [[Templates/New Note|新筆記]]。

更短的步驟見 [[快速上手]]。外掛安裝和「為什麼要裝」見 [[README]]。

## 資料夾

| 資料夾 | 用來放什麼 |
| --- | --- |
| Inbox | 報告原文（PDF、Office、圖片或 Markdown） |
| Parsed | 文件解析得到的 Markdown |
| Tombs | 抽取後的墓葬資料 |
| Sites | 遺址筆記 |
| Artifacts | 器物筆記 |
| Attachments | 圖片和附件 |
| Templates | 配套範本 |

## 示例

庫裡有一份合成示例：[[Inbox/示例墓葬文本]]。開啟它，執行 **Parse archaeological tombs**，應能抽出 M1（土坑豎穴墓，墓口長 2.5 公尺、寬 1.2 公尺、深 3.0 公尺）。這不是真實發掘報告，只用來試命令。

說明：捆綁的墓葬解析器目前依簡體關鍵詞辨認形制和尺寸。這份示例正文因此保持簡體，好讓這條命令在繁體庫裡也能跑通。
