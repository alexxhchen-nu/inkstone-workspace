---
title: README
tags:
  - start
---

# 繁體中文起始庫說明

用 Obsidian「開啟資料夾作為儲存庫」，選本資料夾（倉庫裡的 `vault/zh-Hant/`）。開啟後從 [[Start Here]] 開始。簡體變體在 `vault/zh-Hans/`，結構相同。

更短的步驟見 [[快速上手]]。第三方來源、版本和授權見倉庫根目錄的 `NOTICE.md`。

## 如何安裝 / 啟用外掛

本庫已經打包了下面四個外掛和 Still 主題，開啟後在「設定 → 第三方外掛」裡啟用即可（預設已寫入啟用清單）。

若某個外掛顯示缺失，把官方發布的 `main.js`、`manifest.json`、`styles.css` 放進 `.obsidian/plugins/<外掛 id>/`，然後啟用。不要把 API key 寫進這些檔案。

也可以在 Obsidian 裡瀏覽社群外掛，按 id 搜尋後安裝（自研兩個外掛若尚未上架，繼續用庫內打包的檔案）：

- `archaeo-doc-parser`
- `archaeo-tombs`
- `templater-obsidian`（也可以點 [在 Obsidian 中開啟](obsidian://show-plugin?id=templater-obsidian)）
- `obsidian-style-settings`（[在 Obsidian 中開啟](obsidian://show-plugin?id=obsidian-style-settings)）

主題：設定 → 外觀 → 主題選 **Still**。若主題列表裡沒有，確認 `.obsidian/themes/Still/theme.css` 還在。

## 每個外掛為什麼要

| 外掛 | 為什麼要 |
| --- | --- |
| Archaeo Doc Parser | 把報告 PDF、圖片或 Office 檔轉成 Markdown，供下一步抽取。免費方案可不填 MinerU token。 |
| Archaeological Tomb Parser | 從報告 Markdown 裡抽取墓葬編號、形制、尺寸等，匯出 JSON、CSV、Markdown。 |
| Templater | 插入本庫的業務範本；也可用核心「範本」外掛做同樣的事。 |
| Style Settings | 用來開關 Still 主題的中文排版和字體搭配。 |

自研兩個外掛來自 [alexxhchen-nu/untangle](https://github.com/alexxhchen-nu/untangle)，依 MIT 打包進本庫。Templater 是 AGPL-3.0，Style Settings 是 GPL-3.0，Still 是 MIT；完整出處見 `NOTICE.md`。

## 如何用範本建立筆記

1. 命令面板執行「插入範本」（核心範本）或「Templater: Insert template」。
2. 選 `Templates/New Note.md`、`Report.md`、`Tomb.md`、`Site.md` 或 `Artifact.md`。
3. 填 frontmatter 和正文。建議把遺址筆記放在 `Sites/`，墓葬放在 `Tombs/`，器物放在 `Artifacts/`，報告原文放在 `Inbox/`，解析結果在 `Parsed/`。

外掛輸出路徑已經對準這些資料夾：Doc Parser 寫入 `Parsed/`；Tomb Parser 寫入 `Tombs/<來源檔名>_tombs/`。


## 配色

本庫啟用了 CSS 片段 `.obsidian/snippets/inkstone-palette.css`（設定 → 外觀 → CSS 片段），基礎主題固定為 Obsidian 淺色（`moonstone`），不用深色方案。主色是中國傳統色 **火磚紅** `#cd6227`，色值來自 [zhongguose.com/colors.json](https://zhongguose.com/colors.json)（2026-11-27 讀取）。色庫裡沒有名為「磚紅」的條目，火磚紅是對應的磚紅色。完整色表和對比度見倉庫根目錄 [README](https://github.com/alexxhchen-nu/inkstone-workspace#配色)，預覽圖在 `docs/palette-preview.png`。

| 色名 | Hex | 角色 |
| --- | --- | --- |
| 火磚紅 | `#cd6227` | 主色 / 強調 |
| 赭石 | `#862617` | 懸停、按鈕底 |
| 漢白玉 | `#f8f4ed` | 背景 |
| 珍珠灰 | `#e4dfd7` | 次級背景 |
| 青灰 | `#2b333e` | 正文 |
| 石板灰 | `#624941` | 次級文字 |
| 雁灰 | `#80766e` | 邊框 |
| 蟹蝥紅 | `#b14b28` | 連結 |
| 落英淡粉 | `#f9e8d0` | 高亮 / callout |

正文（青灰在漢白玉上）對比度為 11.64:1，達到 WCAG AA / AAA。火磚紅在漢白玉上只有 3.57:1，所以小字連結改用蟹蝥紅（4.90:1 AA）。

## 建議的工作流程

匯入報告到 [[Inbox]] → 轉 Markdown 到 [[Parsed]] → 抽取墓葬到 [[Tombs]] → 用範本補 [[Sites]] 和器物筆記。

## 可選

若你自己已有 letschips / Crisp 授權，可以另外安裝那些外掛。本庫不打包付費外掛，也不需要它們才能用。

## 不要做的事

- 不要把 MinerU token 或其他密鑰寫進庫、外掛設定備份或筆記。
- 不要把有版權的報告全文或報告圖片提交回這個倉庫。
