# NOTICE

Third-party and first-party components bundled in this repository (`inkstone-workspace`),
under `vault/zh-Hans` and `vault/zh-Hant`.
Do not add API keys, tokens, or credentials to this repository.

## First-party Obsidian plugins (from Untangle)

These files (`main.js`, `manifest.json`, and `styles.css` when present) are copied
from the public repository [alexxhchen-nu/untangle](https://github.com/alexxhchen-nu/untangle)
at commit `2249f296dfb4284ac9f356943daba92f8396fa2a`. This starter is not a fork of Untangle and does not
include the Untangle web app.

| Plugin id | Version | License | Source in Untangle | Upstream files copied |
| --- | --- | --- | --- | --- |
| archaeo-doc-parser | 0.1.0 | MIT | `plugins/obsidian-archaeo-doc-parser/` | `main.js`, `manifest.json`, `LICENSE` |
| archaeo-tombs | 1.0.0 | MIT (stated in the Untangle plugin README, which had no separate LICENSE file; a MIT `LICENSE` with Copyright (c) 2026 Xiaohan Chen is included here so the public bundle ships a license file) | `plugins/obsidian-archaeo-tombs/` | `main.js`, `manifest.json`, `styles.css`, plus `LICENSE` added in this repo |

Corresponding source remains in Untangle at the commit above.
A copy of `tomb_parser.ts` is also kept at `scripts/vendor/tomb_parser.ts` (with `scripts/vendor/LICENSE`) so the sample-parse check can run without a checkout of Untangle.

## Community plugin: Templater

| Field | Value |
| --- | --- |
| Plugin id | templater-obsidian |
| Version | 2.27.0 |
| License | GNU Affero General Public License v3.0 |
| Source | https://github.com/SilentVoid13/Templater |
| Release | https://github.com/SilentVoid13/Templater/releases/tag/2.27.0 |
| Bundled files | `main.js`, `manifest.json`, `styles.css`, `LICENSE.TXT` (verbatim official release) |

Corresponding source: https://github.com/SilentVoid13/Templater/tree/2.27.0

## Community plugin: Style Settings

| Field | Value |
| --- | --- |
| Plugin id | obsidian-style-settings |
| Version | 1.0.9 |
| License | GNU General Public License v3.0 |
| Source | https://github.com/obsidian-community/obsidian-style-settings |
| Release | https://github.com/obsidian-community/obsidian-style-settings/releases/tag/1.0.9 |
| Bundled files | `main.js`, `manifest.json`, `styles.css`, `LICENSE.md` (verbatim official release) |

Corresponding source: https://github.com/obsidian-community/obsidian-style-settings/tree/1.0.9

## Theme: Still

| Field | Value |
| --- | --- |
| Theme name | Still |
| Version | 0.23.11 |
| License | MIT, Copyright (c) 2026 letschips |
| Source | https://github.com/letschips/obsidian-still |
| Bundled files | `theme.css`, `manifest.json`, `LICENSE` (verbatim from `main` at the version in `manifest.json`) |

## Not bundled

Paid Crisp / letschips plugin suites, activation codes, and commercial CSS or
binaries are not included. If you already have a letschips license, you can
install those plugins yourself; they are optional and not required for this vault.
