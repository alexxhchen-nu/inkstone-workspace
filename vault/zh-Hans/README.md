---
title: README
tags:
  - start
---

# 简体中文起始库说明

用 Obsidian「打开文件夹作为库」，选本文件夹（仓库里的 `vault/zh-Hans/`）。打开后从 [[Start Here]] 开始。繁体变体在 `vault/zh-Hant/`，结构相同。

更短的步骤见 [[快速上手]]。第三方来源、版本和许可证见仓库根目录的 `NOTICE.md`。

## 如何安装 / 启用插件

本库已经打包了下面四个插件和 Still 主题，打开后在「设置 → 第三方插件」里启用即可（默认已写入启用清单）。

若某个插件显示缺失，把官方发布的 `main.js`、`manifest.json`、`styles.css` 放进 `.obsidian/plugins/<插件 id>/`，然后启用。不要把 API key 写进这些文件。

也可以在 Obsidian 里浏览社区插件，按 id 搜索后安装（自研两个插件若尚未上架，继续用库内打包的文件）：

- `archaeo-doc-parser`
- `archaeo-tombs`
- `templater-obsidian`（也可以点 [在 Obsidian 中打开](obsidian://show-plugin?id=templater-obsidian)）
- `obsidian-style-settings`（[在 Obsidian 中打开](obsidian://show-plugin?id=obsidian-style-settings)）

主题：设置 → 外观 → 主题选 **Still**。若主题列表里没有，确认 `.obsidian/themes/Still/theme.css` 还在。

## 每个插件为什么要

| 插件 | 为什么要 |
| --- | --- |
| Archaeo Doc Parser | 把报告 PDF、图片或 Office 文件转成 Markdown，供下一步抽取。免费档可不填 MinerU token。 |
| Archaeological Tomb Parser | 从报告 Markdown 里抽取墓葬编号、形制、尺寸等，导出 JSON、CSV、Markdown。 |
| Templater | 插入本库的业务模板；也可用核心「模板」插件做同样的事。 |
| Style Settings | 用来开关 Still 主题的中文排版和字体搭配。 |

自研两个插件来自 [alexxhchen-nu/untangle](https://github.com/alexxhchen-nu/untangle)，按 MIT 打包进本库。Templater 是 AGPL-3.0，Style Settings 是 GPL-3.0，Still 是 MIT；完整出处见 `NOTICE.md`。

## 如何用模板建笔记

1. 命令面板运行「插入模板」（核心模板）或「Templater: Insert template」。
2. 选 `Templates/New Note.md`、`Report.md`、`Tomb.md`、`Site.md` 或 `Artifact.md`。
3. 填 frontmatter 和正文。建议把遗址笔记放在 `Sites/`，墓葬放在 `Tombs/`，器物放在 `Artifacts/`，报告原文放在 `Inbox/`，解析结果在 `Parsed/`。

插件输出路径已经对准这些文件夹：Doc Parser 写入 `Parsed/`；Tomb Parser 写入 `Tombs/<源文件名>_tombs/`。


## 配色

本库启用了 CSS 片段 `.obsidian/snippets/inkstone-palette.css`（设置 → 外观 → CSS 片段），基础主题固定为 Obsidian 浅色（`moonstone`），不用深色方案。主色是中国传统色 **火砖红** `#cd6227`，色值来自 [zhongguose.com/colors.json](https://zhongguose.com/colors.json)（2026-11-27 读取）。色库里没有名为「砖红」的条目，火砖红是对应的砖红色。完整色表和对比度见仓库根目录 [README](https://github.com/alexxhchen-nu/inkstone-workspace#配色)，预览图在 `docs/palette-preview.png`。

| 色名 | Hex | 角色 |
| --- | --- | --- |
| 火砖红 | `#cd6227` | 主色 / 强调 |
| 赭石 | `#862617` | 悬停、按钮底 |
| 汉白玉 | `#f8f4ed` | 背景 |
| 珍珠灰 | `#e4dfd7` | 次级背景 |
| 青灰 | `#2b333e` | 正文 |
| 石板灰 | `#624941` | 次级文字 |
| 雁灰 | `#80766e` | 边框 |
| 蟹蝥红 | `#b14b28` | 链接 |
| 落英淡粉 | `#f9e8d0` | 高亮 / callout |

正文（青灰在汉白玉上）对比度为 11.64:1，达到 WCAG AA / AAA。火砖红在汉白玉上只有 3.57:1，所以小字链接改用蟹蝥红（4.90:1 AA）。

## 建议的工作流

导入报告到 [[Inbox]] → 转 Markdown 到 [[Parsed]] → 抽取墓葬到 [[Tombs]] → 用模板补 [[Sites]] 和器物笔记。

## 可选

若你自己已有 letschips / Crisp 许可，可以另外安装那些插件。本库不打包付费插件，也不需要它们才能用。

## 不要做的事

- 不要把 MinerU token 或其他密钥写进库、插件设置备份或笔记。
- 不要把有版权的报告全文或报告图片提交回这个仓库。
