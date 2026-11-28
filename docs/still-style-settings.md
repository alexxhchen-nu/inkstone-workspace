# Still 主题的 Style Settings 选项

本页从本库捆绑的 Still 主题 `theme.css` 里的 `@settings` 块整理，对应版本 **0.23.11**（`vault/*/.obsidian/themes/Still/manifest.json`）。
在 Obsidian 里用 [Style Settings](https://github.com/obsidian-community/obsidian-style-settings)（本库已捆绑 1.0.9）编辑：命令面板运行 **Show style settings view**，或打开设置里的 Style Settings。

本库只预置了一项与主题默认值不同的选择：`still-cjk`（中文排版）为开启，见两个库的 `.obsidian/plugins/obsidian-style-settings/data.json`。其余选项保持主题默认，未写入 `data.json`。

本库基础主题固定为浅色（`moonstone`）。下表仍列出主题自带的深色相关选项（例如 PDF 深色、深色背景图 CSS），以便对照 Style Settings 里实际出现的项目；起始库本身没有提供深色配色方案。

## 分组一览

| 分组 | 选项数 | Style Settings id |
| --- | ---: | --- |
| 阅读 / Reading | 12 | `still-heading-reading` |
| 颜色 / Colors | 23 | `still-heading-colors` |
| 文字高亮 / Text highlights | 7 | `still-heading-highlights` |
| 界面 / Interface | 21 | `still-heading-interface` |
| 内容 / Content | 16 | `still-heading-content` |

## 阅读 / Reading

分组 id：`still-heading-reading`

| id | 名称（中 / 英） | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `still-line-width` | 行宽 / Line width | 数值滑块 | `700` | 开启「缩减栏宽」时的正文宽度。 |
| `still-line-height` | 行高 / Line height | 数值滑块 | `1.625` |  |
| `still-paragraph-spacing` | 段落间距 / Paragraph spacing | 数值滑块 | `1.25` |  |
| `still-list-spacing` | 列表项间距 / List item spacing | 数值滑块 | `0.175` |  |
| `still-centered-title` | 笔记标题居中 / Centered note title | 开关（class-toggle） | `false` |  |
| `still-cjk` | 中文排版 / CJK typography | 开关（class-toggle） | `false` | 适合中文和日文写作。中文与英文、数字相邻且没打空格时自动留出小间隙；优化阅读视图的段落断行，iOS 正文保留普通换行；默认行高放宽到 1.75。代码保持原样。单篇笔记可在 cssclasses 写 cjk / no-cjk 单独开关。 |
| `still-justify` | 两端对齐 / Justified paragraphs | 开关（class-toggle） | `false` | 正文在阅读和编辑视图中两端对齐，符合中文排版习惯。标题、代码和表格不受影响。英文较多的段落词距可能被拉大。单篇笔记可在 cssclasses 写 justify / no-justify 单独开关。 |
| `still-indent` | 首行缩进 / First-line indent | 开关（class-toggle） | `false` | 正文段落首行缩进两个字，阅读视图和实时预览都生效。列表、引用、提示块、表格和代码不缩进。单篇笔记可在 cssclasses 写 indent / no-indent 单独开关。 |
| `still-fonts` | 中文字体搭配 / Chinese font pairing | 下拉（class-select） | `still-fonts-off` | 只用系统自带字体，不下载任何东西。「黑体」让系统语言不是中文时也显示中文字形；「宋体」把正文换成宋体，标题用黑体、引用用楷体（移动端需系统已安装对应字体）。在「设置 → 外观」里选的字体仍然优先。 |
|  | 可选项 |  |  | Off · 关闭 → `still-fonts-off`；Hei · 黑体 → `still-fonts-hei`；Song · 宋体 → `still-fonts-song` |
| `still-highlight-strong` | 加深文字高亮 / Stronger text highlight | 开关（class-toggle） | `false` | 加深阅读视图和实时预览中的文字高亮颜色。 |
| `still-active-line` | 当前编辑行提示 / Active line highlight | 开关（class-toggle） | `false` | 编辑器获得焦点时，为当前正文行加一层淡底色。引用和代码保留原有背景。 |
| `still-link-underline` | 链接常显下划线 / Underline links | 开关（class-toggle） | `false` | 在阅读和编辑视图中，为笔记链接和网页链接保留下划线，不只靠颜色辨认。单篇笔记可在 cssclasses 写 link-underline / no-link-underline 单独开关。 |

## 颜色 / Colors

分组 id：`still-heading-colors`

| id | 名称（中 / 英） | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `still-preset` | 配方 / Preset | 下拉（class-select） | `still-preset-off` | 现成的一套浅色和深色配色。选中时，下方的窗口背景、页面、侧栏、正文和次要文字颜色由它决定；选「关闭」才用你自己设的。纹理和渐变画在窗口背景上，要打开「窗口背景」才看得到。 |
|  | 可选项 |  |  | Off · 关闭 → `still-preset-off`；Paper · 类纸 → `still-preset-paper`；Mist · 雾灰 → `still-preset-mist`；Sand · 暖砂 → `still-preset-sand`；Sage · 苔绿 → `still-preset-sage`；Graphite · 石墨 → `still-preset-graphite`；Night · 夜航 → `still-preset-night` |
| `still-preset-accent` | 配方强调色 / Preset accent | 开关（class-toggle） | `false` | 选了配方时，按钮、链接、标签和选中底色改用这套配方自己的色调，不再用「设置 → 外观」里的强调色。 |
| `still-preset-texture` | 配方质感 / Preset texture | 下拉（class-select） | `still-texture-preset` | 选了配方时，「平滑」去掉颗粒，「磨砂」铺一层细纹，「斑驳」叠加不均匀的淡斑和细颗粒，都保留配方原有的渐变。要打开「窗口背景」才看得到；手机和平板上只有颜色。 |
|  | 可选项 |  |  | Preset · 跟随配方 → `still-texture-preset`；Smooth · 平滑 → `still-texture-smooth`；Frosted · 磨砂 → `still-texture-frosted`；Mottled · 斑驳 → `still-texture-mottled` |
| `still-page-color` | 页面背景 / Page background | 浅色/深色颜色 | （空） |  |
| `still-sidebar-color` | 侧栏背景 / Sidebar background | 浅色/深色颜色 | （空） |  |
| `still-backdrop` | 窗口背景 / Window background | 下拉（class-select） | `still-backdrop-off` | 在整个窗口底下铺一层背景，边框区域变透明来透出它。「边框」时页面保留自己的底色，「整窗」时页面也透出背景。手机和平板上只沿用背景色：侧栏用它，「整窗」时页面也用它。 |
|  | 可选项 |  |  | Off · 关闭 → `still-backdrop-off`；Frame · 边框 → `still-backdrop-frame`；Whole window · 整窗 → `still-backdrop-window` |
| `still-backdrop-color` | 窗口背景色 / Window background color | 浅色/深色颜色 | （空） | 默认用侧栏背景色。调低不透明度，半透明窗口会透出来。 |
| `still-backdrop-css-light` | 窗口背景 CSS（浅色） / Window background CSS (light) | 文本 | （空） | 可选。任意 CSS background 值，叠在背景色上面：渐变，或纹理，例如 #fffcf0 url("data:image/png;base64,…")。 |
| `still-backdrop-css-dark` | 窗口背景 CSS（深色） / Window background CSS (dark) | 文本 | （空） | 可选。深色模式用的背景。 |
| `still-text-color` | 正文文字 / Text | 浅色/深色颜色 | （空） |  |
| `still-muted-color` | 次要文字 / Secondary text | 浅色/深色颜色 | （空） |  |
| `still-link-color` | 链接 / Links | 浅色/深色颜色 | （空） | 默认使用强调色。 |
| `still-list-marker-color` | 列表符号 / List markers | 浅色/深色颜色 | （空） | 默认使用浅色文字。 |
| `still-checkbox-color` | 复选框 / Checkboxes | 浅色/深色颜色 | （空） | 默认使用强调色。 |
| `still-h1-color` | 一级标题 / Heading 1 | 浅色/深色颜色 | （空） | 开不开「彩色标题」都生效。笔记标题仍用正文颜色。 |
| `still-h2-color` | 二级标题 / Heading 2 | 浅色/深色颜色 | （空） |  |
| `still-h3-color` | 三级标题 / Heading 3 | 浅色/深色颜色 | （空） |  |
| `still-h4-color` | 四级标题 / Heading 4 | 浅色/深色颜色 | （空） |  |
| `still-h5-color` | 五级标题 / Heading 5 | 浅色/深色颜色 | （空） |  |
| `still-h6-color` | 六级标题 / Heading 6 | 浅色/深色颜色 | （空） |  |
| `still-table-head-color` | 表头文字 / Table header text | 浅色/深色颜色 | （空） |  |
| `still-table-head-bg` | 表头底色 / Table header background | 浅色/深色颜色 | （空） | 开启「表格只留横线」时同样生效。 |
| `still-graphite` | 石墨墨色 / Graphite ink | 开关（class-toggle） | `false` | 按钮、开关和链接改用文字颜色而不是强调色，链接加下划线。 |

## 文字高亮 / Text highlights

分组 id：`still-heading-highlights`

| id | 名称（中 / 英） | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `still-highlight-color` | 默认高亮 / Default highlight | 浅色/深色颜色 | （空） | 用于 ==文字== 的高亮底色，自动按高亮透明度混合，可与「加深文字高亮」联动。 |
| `still-highlight-red` | 红色高亮 / Red highlight | 浅色/深色颜色 | （空） |  |
| `still-highlight-orange` | 橙色高亮 / Orange highlight | 浅色/深色颜色 | （空） |  |
| `still-highlight-yellow` | 黄色高亮 / Yellow highlight | 浅色/深色颜色 | （空） |  |
| `still-highlight-green` | 绿色高亮 / Green highlight | 浅色/深色颜色 | （空） |  |
| `still-highlight-blue` | 蓝色高亮 / Blue highlight | 浅色/深色颜色 | （空） |  |
| `still-highlight-purple` | 紫色高亮 / Purple highlight | 浅色/深色颜色 | （空） |  |

## 界面 / Interface

分组 id：`still-heading-interface`

| id | 名称（中 / 英） | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `still-roundness` | 圆角 / Roundness | 数值滑块 | `1.25` | 按比例缩放所有圆角，0 为直角。 |
| `still-compact` | 紧凑界面 / Compact interface | 开关（class-toggle） | `false` | 标题栏和标签更矮，侧栏、菜单和设置的行距更紧，适合小屏幕。正文排版不变。仅电脑端。 |
| `still-flat-page` | 平铺页面 / Flat page | 开关（class-toggle） | `false` | 默认在侧栏展开时，页面像卡片一样浮起。 |
| `still-tabs-left` | 标签靠左 / Left-aligned tabs | 开关（class-toggle） | `false` | 默认标签居中。 |
| `still-tabs-fit` | 标签宽度随标题 / Tabs fit their titles | 开关（class-toggle） | `false` | 默认所有标签等宽。 |
| `still-header-title` | 标题栏始终显示笔记标题 / Always show the note title in the header | 开关（class-toggle） | `false` | 默认鼠标移到标题栏时才显示。 |
| `still-peek-off` | 关闭侧栏悬停展开 / Disable sidebar peek | 开关（class-toggle） | `false` | 默认鼠标停在窗口边缘时，收起的侧栏会滑出。 |
| `still-peek-soft` | 柔和侧栏展开 / Soft sidebar peek | 开关（class-toggle） | `false` | 滑出的侧栏柔和地渐隐到页面里，没有阴影边。 |
| `still-peek-ribbon` | 自动隐藏功能区 / Auto-hide ribbon | 开关（class-toggle） | `false` | 鼠标移到窗口左缘时才显示左侧功能区。 |
| `still-hide-vault` | 安静的库切换器 / Quiet vault switcher | 开关（class-toggle） | `false` | 库信息浮在侧栏底部，只留设置按钮；鼠标移上去才显示库名。帮助可在命令面板搜索「查看帮助」打开。 |
| `still-hide-vault-settings` | 设置按钮也隐藏 / Hide the Settings button too | 开关（class-toggle） | `false` | 配合「安静的库切换器」使用：设置按钮位置不变，平时不显示，鼠标移上去才出现。 |
| `still-quiet-nav` | 安静的侧栏工具栏 / Quiet sidebar toolbar | 开关（class-toggle） | `false` | 侧栏工具栏按钮平时显示为小圆点，悬停时展开；手机和平板上点一下圆点展开。 |
| `still-quiet-header` | 安静的视图标题栏 / Quiet view header | 开关（class-toggle） | `false` | 笔记视图标题栏里的返回、前进和右侧动作按钮平时隐藏，在电脑端及外接指针设备的平板上悬停或聚焦时显现。网页浏览器和堆叠标签页保持显示。 |
| `still-quiet-tab-actions` | 安静的顶栏按钮 / Quiet tab bar buttons | 开关（class-toggle） | `false` | 顶栏两侧的侧栏开关、新建标签和标签列表按钮平时隐藏，在电脑端及外接指针设备的平板上悬停或聚焦时显现。 |
| `still-quiet-status` | 安静的状态栏 / Quiet status bar | 开关（class-toggle） | `false` | 状态栏平时隐藏，鼠标靠近底部中间时出现。 |
| `still-status-always` | 状态栏始终显示 / Always show the status bar | 开关（class-toggle） | `false` | 开启「安静的状态栏」后，让电脑端底部胶囊始终显示。 |
| `still-outline-guides` | 大纲层级线 / Outline guides | 开关（class-toggle） | `false` | 大纲面板每一级标题显示一条细线，鼠标所在标题下的分支线条加深。 |
| `still-motion-off` | 关闭入场动画 / Disable entrance motion | 开关（class-toggle） | `false` | 菜单、浮窗和对话框直接出现，不再淡入上浮。 |
| `still-black-mobile` | 手机和平板纯黑 / Pure black on phones and tablets | 开关（class-toggle） | `false` | 移动端深色模式下页面和侧栏使用纯黑，适合 OLED 屏幕。 |
| `still-full-drawers` | 手机侧栏全屏 / Full-screen sidebars on phones | 开关（class-toggle） | `false` | 滑出的侧栏铺满整屏，旁边不再露出一截笔记。iPad 分屏等窄窗口同样生效。 |
| `still-push-drawers` | 手机侧栏推开笔记 / Sidebars stay put on phones | 开关（class-toggle） | `false` | 配合 Obsidian 的「滑动侧栏」设置：侧栏留在底层不动，笔记像一张卡片被推开。开启「手机侧栏全屏」时自动停用。 |

## 内容 / Content

分组 id：`still-heading-content`

| id | 名称（中 / 英） | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `still-quiet-properties` | 安静的笔记属性 / Quiet properties | 开关（class-toggle） | `false` | 笔记属性改为紧凑的低对比排版并加底部细线；电脑端及外接指针设备的平板上类型图标和「添加属性」悬停时才出现。单篇笔记可在 cssclasses 写 quiet-properties / no-quiet-properties 单独开关。 |
| `still-properties-columns` | 双列笔记属性 / Two-column properties | 开关（class-toggle） | `false` | 页面够宽时将笔记属性排成两列，标签和列表字段占满整行；窄屏自动恢复单列。单篇笔记可在 cssclasses 写 compact-properties / no-compact-properties 单独开关。 |
| `still-card-callouts` | 卡片式提示块 / Card callouts | 开关（class-toggle） | `false` | 标题放在着色的外框上，内容放在内层卡片里。 |
| `still-plain-tags` | 纯文字标签 / Plain tags | 开关（class-toggle） | `false` | 标签显示为彩色文字，不带底色。 |
| `still-keep-done-tasks` | 已完成任务不加删除线 / Don't strike completed tasks | 开关（class-toggle） | `false` |  |
| `still-colored-headings` | 彩色标题 / Colored headings | 开关（class-toggle） | `false` | 每级标题一种颜色，从 H1 的红色到 H6 的紫色。 |
| `still-media-fill` | 图片铺满行宽 / Images fill the line width | 开关（class-toggle） | `false` | 没有设定宽度的图片、视频和嵌入内容拉伸到行宽，过高的会限制在窗口内。 |
| `still-table-plain` | 表格只留横线 / Hairline tables | 开关（class-toggle） | `false` | 表格去掉外框和表头底色，只保留行与行之间的横线。 |
| `still-table-full` | 表格铺满行宽 / Tables fill the line width | 开关（class-toggle） | `false` | 表格和正文一样宽，左右与正文对齐。用了 table-wide 的笔记保持自己的宽度。 |
| `still-table-auto` | 宽表格自动加宽 / Wide tables grow | 开关（class-toggle） | `false` | 比正文宽的表格按需向两侧展开，最宽到页面宽度，再宽就左右滑动；比正文窄的表格不变。需要开启「缩减栏宽」；用了 table-wide 的笔记保持自己的宽度。 |
| `still-table-cols` | 表格显示列线 / Column lines in tables | 开关（class-toggle） | `false` | 所有表格的列与列之间加细线，相当于给每篇笔记都写上 col-lines。 |
| `still-bases-stripes` | Bases 表格隔行条纹 / Striped Bases tables | 开关（class-toggle） | `false` | Bases 表格每隔一行加一层浅色底。 |
| `still-canvas-plain` | Canvas 无点阵背景 / Plain Canvas background | 开关（class-toggle） | `false` |  |
| `still-pdf-dark` | 深色 PDF / Dark PDFs | 开关（class-toggle） | `false` | 深色模式下反色显示 PDF 页面。 |
| `still-pdf-dim` | 深色模式 PDF 降亮 / Dim PDFs in dark mode | 开关（class-toggle） | `false` | 深色模式下 PDF 页面平时调暗，悬停或触屏按住时恢复。 |
| `still-img-dim` | 深色模式图片降亮 / Dim images in dark mode | 开关（class-toggle） | `false` | 深色模式下笔记里的图片平时调暗，悬停或触屏按住时恢复。链接图标不受影响。 |

## 单篇笔记覆盖

部分排版开关支持在笔记 frontmatter 的 `cssclasses` 里按篇覆盖（摘自主题说明原文）：

- 中文排版：`cjk` / `no-cjk`
- 两端对齐：`justify` / `no-justify`
- 首行缩进：`indent` / `no-indent`
- 链接常显下划线：`link-underline` / `no-link-underline`

来源：Still `theme.css` 中对应选项的 `description.zh`。

