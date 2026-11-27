#!/usr/bin/env python3
"""Validate the zh-Hans / zh-Hant Obsidian starter vaults."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VARIANTS = ("zh-Hans", "zh-Hant")
VAULT_ROOT = ROOT / "vault"

REQUIRED_RELATIVE_PATHS = [
    "Start Here.md",
    "快速上手.md",
    "README.md",
    "Inbox/示例墓葬文本.md",
    "Templates/New Note.md",
    "Templates/Report.md",
    "Templates/Tomb.md",
    "Templates/Site.md",
    "Templates/Artifact.md",
    ".obsidian/app.json",
    ".obsidian/appearance.json",
    ".obsidian/community-plugins.json",
    ".obsidian/core-plugins.json",
    ".obsidian/core-plugins-migration.json",
    ".obsidian/templates.json",
    ".obsidian/snippets/inkstone-palette.css",
    ".gitignore",
]

REQUIRED_DIRS = [
    "Inbox",
    "Parsed",
    "Tombs",
    "Sites",
    "Artifacts",
    "Attachments",
    "Templates",
    ".obsidian/plugins",
    ".obsidian/themes/Still",
]

TEMPLATE_REQUIRED_FM = {
    "Templates/New Note.md": {"type", "title", "tags"},
    "Templates/Report.md": {"type", "title", "period", "site", "source", "tags"},
    "Templates/Tomb.md": {
        "type",
        "title",
        "site",
        "tomb_id",
        "period",
        "orientation",
        "form",
        "length_m",
        "width_m",
        "depth_m",
        "source",
        "tags",
    },
    "Templates/Site.md": {"type", "title", "period", "location", "source", "tags"},
    "Templates/Artifact.md": {
        "type",
        "title",
        "site",
        "tomb_id",
        "material",
        "form",
        "count",
        "source",
        "tags",
    },
}

FORBIDDEN_COMMITTED = {
    ".obsidian/workspace.json",
    ".obsidian/workspace-mobile.json",
    ".obsidian/workspaces.json",
    ".obsidian/cache",
}

WIKILINK_RE = re.compile(r"(?<!`)(!?\[\[)([^\]]+)\]\]")
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)

# High-signal secret patterns. Mentions of the word "token" in docs are allowed.
SECRET_LINE_RE = re.compile(
    r"(?i)("
    r"(mineruToken\"\s*:\s*\"[^\"]+\")"
    r"|(api[_-]?key|secret[_-]?key|access[_-]?token|auth[_-]?token)"
    r"\s*[:=]\s*['\"][^'\"]{8,}['\"]"
    r"|(sk-live|sk-ant-|ghp_|github_pat_|xox[baprs]-|AKIA)[A-Za-z0-9/_+=-]+"
    r"|(-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----)"
    r")"
)

ENABLED_CORE = {
    "file-explorer",
    "global-search",
    "switcher",
    "graph",
    "backlink",
    "canvas",
    "outgoing-link",
    "properties",
    "page-preview",
    "templates",
    "note-composer",
    "command-palette",
    "slash-command",
    "editor-status",
    "bookmarks",
    "outline",
    "word-count",
    "file-recovery",
    "bases",
}
DISABLED_CORE = {
    "tag-pane",
    "footnotes",
    "daily-notes",
    "markdown-importer",
    "zk-prefixer",
    "random-note",
    "slides",
    "audio-recorder",
    "workspaces",
    "publish",
    "sync",
    "webviewer",
}



def _rel_lum(rgb: tuple[int, int, int]) -> float:
    def chan(c: int) -> float:
        x = c / 255
        return x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4
    r, g, b = rgb
    return 0.2126 * chan(r) + 0.7152 * chan(g) + 0.0722 * chan(b)


def contrast_ratio(h1: str, h2: str) -> float:
    def to_rgb(h: str) -> tuple[int, int, int]:
        h = h.lstrip("#")
        return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    l1, l2 = _rel_lum(to_rgb(h1)), _rel_lum(to_rgb(h2))
    return (max(l1, l2) + 0.05) / (min(l1, l2) + 0.05)


class Failures(list):
    def add(self, msg: str) -> None:
        self.append(msg)


def parse_frontmatter(text: str) -> dict | None:
    m = FM_RE.match(text)
    if not m:
        return None
    data: dict = {}
    key = None
    for raw in m.group(1).splitlines():
        line = raw.rstrip()
        if not line.strip() or line.strip().startswith("#"):
            continue
        if line.startswith("  - ") and key:
            data.setdefault(key, [])
            if not isinstance(data[key], list):
                data[key] = []
            data[key].append(_unquote(line[4:].strip()))
            continue
        if ":" in line and not line.startswith(" "):
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            data[key] = [] if val == "" and False else (_unquote(val) if val else "")
    return data


def _unquote(val: str):
    if len(val) >= 2 and val[0] == val[-1] and val[0] in {'"', "'"}:
        return val[1:-1]
    if val in {"true", "false"}:
        return val == "true"
    return val


def iter_json_files(obsidian: Path):
    for path in sorted(obsidian.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() != ".json":
            continue
        if "cache" in path.parts:
            continue
        yield path


def wiki_target(raw: str) -> str | None:
    body = raw.strip()
    if not body:
        return None
    if "|" in body:
        body = body.split("|", 1)[0].strip()
    if "#" in body:
        body = body.split("#", 1)[0].strip()
    return body or None


def resolve_link(vault: Path, current: Path, target: str) -> bool:
    target = target.replace("\\", "/").rstrip("/")
    candidates = []
    if target.startswith("/"):
        rel = target.lstrip("/")
        candidates.append(vault / rel)
        candidates.append(vault / f"{rel}.md")
    else:
        candidates.append(vault / target)
        candidates.append(vault / f"{target}.md")
        # Obsidian also resolves by note name anywhere in the vault.
        name = Path(target).name
        candidates.append(vault / name)
        candidates.append(vault / f"{name}.md")
        # relative to the current file's folder
        rel_base = current.parent / target
        candidates.append(rel_base)
        candidates.append(Path(str(rel_base) + ".md"))
    for cand in candidates:
        try:
            cand.resolve().relative_to(vault.resolve())
        except ValueError:
            continue
        if cand.exists():
            return True
    # Filename match (unique note title)
    stem = Path(target).name
    if stem.endswith(".md"):
        stem = stem[:-3]
    matches = [p for p in vault.rglob("*.md") if p.stem == stem]
    return len(matches) >= 1


def check_secrets(root: Path, failures: Failures) -> None:
    skip_parts = {".git", "node_modules", ".venv"}
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in skip_parts for part in path.parts):
            continue
        if path.suffix.lower() in {".js", ".css", ".txt", ".md"} and (
            "plugins" in path.parts or "themes" in path.parts or path.name.startswith("LICENSE")
        ):
            # Vendored upstream files may mention "license key" in legal text; still
            # scan plugin data.json and our notes.
            if path.name not in {"data.json"} and "LICENSE" not in path.name.upper() and path.suffix in {".js", ".css", ".txt"}:
                continue
            if "LICENSE" in path.name.upper():
                continue
            if path.suffix in {".js", ".css"}:
                continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            if SECRET_LINE_RE.search(line):
                failures.add(f"possible secret {path.relative_to(root)}:{i}")


def check_vault(vault: Path, failures: Failures) -> set[str]:
    rel_files: set[str] = set()
    for path in vault.rglob("*"):
        if path.is_file():
            rel_files.add(path.relative_to(vault).as_posix())

    for rel in REQUIRED_RELATIVE_PATHS:
        if rel not in rel_files:
            failures.add(f"{vault.name}: missing {rel}")
    for rel in REQUIRED_DIRS:
        if not (vault / rel).is_dir():
            failures.add(f"{vault.name}: missing directory {rel}")
    for rel in FORBIDDEN_COMMITTED:
        if (vault / rel).exists():
            failures.add(f"{vault.name}: should not commit {rel}")

    obsidian = vault / ".obsidian"
    for path in iter_json_files(obsidian):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            failures.add(f"{vault.name}: invalid JSON {path.relative_to(vault)}: {exc}")

    try:
        community = json.loads((obsidian / "community-plugins.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        community = []
        failures.add(f"{vault.name}: cannot read community-plugins.json")
    if not isinstance(community, list):
        failures.add(f"{vault.name}: community-plugins.json must be a list")
        community = []
    for plugin_id in community:
        folder = obsidian / "plugins" / plugin_id
        manifest = folder / "manifest.json"
        if not folder.is_dir():
            failures.add(f"{vault.name}: plugin folder missing for {plugin_id}")
            continue
        if not manifest.is_file():
            failures.add(f"{vault.name}: manifest.json missing for {plugin_id}")
            continue
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            failures.add(f"{vault.name}: {plugin_id} manifest is not JSON: {exc}")
            continue
        if data.get("id") != plugin_id:
            failures.add(
                f"{vault.name}: manifest id {data.get('id')!r} != folder {plugin_id!r}"
            )
        main_js = folder / "main.js"
        if not main_js.is_file():
            failures.add(f"{vault.name}: main.js missing for {plugin_id}")
        license_files = list(folder.glob("LICENSE*")) + list(folder.glob("license*"))
        if not license_files:
            failures.add(f"{vault.name}: LICENSE file missing for {plugin_id}")

    appearance = json.loads((obsidian / "appearance.json").read_text(encoding="utf-8"))
    if appearance.get("cssTheme") != "Still":
        failures.add(f"{vault.name}: cssTheme should be Still")
    snippets = appearance.get("enabledCssSnippets") or []
    if "inkstone-palette" not in snippets:
        failures.add(f"{vault.name}: inkstone-palette snippet not enabled")
    snippet = obsidian / "snippets" / "inkstone-palette.css"
    if snippet.is_file() and "#cd6227" not in snippet.read_text(encoding="utf-8"):
        failures.add(f"{vault.name}: palette snippet missing 火砖红 #cd6227")
    still = obsidian / "themes" / "Still"
    if not (still / "theme.css").is_file() or not (still / "manifest.json").is_file():
        failures.add(f"{vault.name}: Still theme files missing")
    if not list(still.glob("LICENSE*")):
        failures.add(f"{vault.name}: Still theme LICENSE missing")

    core = json.loads((obsidian / "core-plugins.json").read_text(encoding="utf-8"))
    for name in ENABLED_CORE:
        if core.get(name) is not True:
            failures.add(f"{vault.name}: core plugin {name} should be enabled")
    for name in DISABLED_CORE:
        if core.get(name) is not False:
            failures.add(f"{vault.name}: core plugin {name} should be disabled")

    templates = json.loads((obsidian / "templates.json").read_text(encoding="utf-8"))
    if templates.get("folder") != "Templates":
        failures.add(f"{vault.name}: templates.json folder should be Templates")

    doc_data = json.loads(
        (obsidian / "plugins" / "archaeo-doc-parser" / "data.json").read_text(encoding="utf-8")
    )
    if doc_data.get("outputFolder") != "Parsed":
        failures.add(f"{vault.name}: doc parser outputFolder should be Parsed")
    if doc_data.get("mineruToken"):
        failures.add(f"{vault.name}: mineruToken must be empty")

    tombs_data = json.loads(
        (obsidian / "plugins" / "archaeo-tombs" / "data.json").read_text(encoding="utf-8")
    )
    if tombs_data.get("outputFolder") != "Tombs":
        failures.add(f"{vault.name}: tombs outputFolder should be Tombs")

    templater = json.loads(
        (obsidian / "plugins" / "templater-obsidian" / "data.json").read_text(encoding="utf-8")
    )
    if templater.get("templates_folder") != "Templates":
        failures.add(f"{vault.name}: Templater templates_folder should be Templates")
    if templater.get("enable_system_commands"):
        failures.add(f"{vault.name}: Templater system commands must stay off")

    for rel, keys in TEMPLATE_REQUIRED_FM.items():
        path = vault / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm is None:
            failures.add(f"{vault.name}: {rel} is missing YAML frontmatter")
            continue
        missing = keys - set(fm)
        if missing:
            failures.add(f"{vault.name}: {rel} missing frontmatter keys {sorted(missing)}")
        if not text.endswith("\n"):
            failures.add(f"{vault.name}: {rel} should end with a newline")

    md_files = [p for p in vault.rglob("*.md") if p.is_file()]
    for path in md_files:
        rel = path.relative_to(vault).as_posix()
        text = path.read_text(encoding="utf-8")
        if rel.startswith("Templates/") and parse_frontmatter(text) is None:
            failures.add(f"{vault.name}: template {rel} has no frontmatter")
        for match in WIKILINK_RE.finditer(text):
            raw = match.group(2)
            target = wiki_target(raw)
            if target is None:
                if rel.startswith("Templates/"):
                    continue
                failures.add(f"{vault.name}: empty wikilink in {rel}")
                continue
            if not resolve_link(vault, path, target):
                failures.add(f"{vault.name}: unresolved [[{target}]] in {rel}")

    return rel_files


def collect_parity_keys(vault: Path) -> set[str]:
    keys = set()
    skip = {".obsidian"}
    for path in vault.rglob("*"):
        rel = path.relative_to(vault)
        if rel.parts and rel.parts[0] in skip:
            # Compare config file names, not vendored binaries already checked.
            if path.suffix.lower() == ".json" and path.is_file():
                keys.add(rel.as_posix())
            elif path.is_dir() and rel.as_posix() in {
                ".obsidian/plugins",
                ".obsidian/themes",
                ".obsidian/themes/Still",
            }:
                keys.add(rel.as_posix() + "/")
            continue
        if path.is_dir():
            if any(path.iterdir()):
                keys.add(rel.as_posix() + "/")
            else:
                keys.add(rel.as_posix() + "/")
        else:
            keys.add(rel.as_posix())
    return keys


def main() -> int:
    failures = Failures()
    if not VAULT_ROOT.is_dir():
        print(f"FAIL: missing {VAULT_ROOT}", file=sys.stderr)
        return 1

    file_maps: dict[str, set[str]] = {}
    for name in VARIANTS:
        vault = VAULT_ROOT / name
        if not vault.is_dir():
            failures.add(f"missing vault {name}")
            continue
        check_vault(vault, failures)
        file_maps[name] = collect_parity_keys(vault)

    if all(v in file_maps for v in VARIANTS):
        hans, hant = file_maps["zh-Hans"], file_maps["zh-Hant"]
        only_hans = sorted(hans - hant)
        only_hant = sorted(hant - hans)
        if only_hans or only_hant:
            failures.add(f"path parity mismatch only in zh-Hans: {only_hans}")
            failures.add(f"path parity mismatch only in zh-Hant: {only_hant}")
        # Config JSON (except style-settings values we keep identical) must match.
        for rel in sorted(
            p
            for p in hans & hant
            if p.startswith(".obsidian/") and p.endswith(".json") and "plugins/" not in p[11:] or False
        ):
            if "/plugins/" in rel and rel.endswith("data.json"):
                # data.json should be identical across variants for these plugins
                pass
        for rel in sorted(p for p in hans & hant if p.startswith(".obsidian/") and p.endswith(".json")):
            a = (VAULT_ROOT / "zh-Hans" / rel).read_text(encoding="utf-8")
            b = (VAULT_ROOT / "zh-Hant" / rel).read_text(encoding="utf-8")
            if json.loads(a) != json.loads(b):
                failures.add(f"config parity mismatch: {rel}")


    # Body-text contrast (WCAG AA 4.5:1). 火砖红 on light is intentionally
    # not in this list; light links use 蟹蝥红 instead.
    body_pairs = [
        ("light body", "#2b333e", "#f8f4ed", 4.5),
        ("light muted", "#624941", "#f8f4ed", 4.5),
        ("light muted on secondary", "#624941", "#e4dfd7", 4.5),
        ("light link", "#b14b28", "#f8f4ed", 4.5),
        ("dark body", "#f8f4ed", "#131824", 4.5),
        ("dark muted", "#a49c93", "#131824", 4.5),
        ("dark link / 火砖红", "#cd6227", "#131824", 4.5),
        ("light button label", "#fffef9", "#862617", 4.5),
    ]
    ui_pairs = [
        ("light accent UI", "#cd6227", "#f8f4ed", 3.0),
        ("light border UI", "#80766e", "#f8f4ed", 3.0),
        ("dark border UI", "#80766e", "#131824", 3.0),
    ]
    for label, a, b, min_ratio in body_pairs + ui_pairs:
        ratio = contrast_ratio(a, b)
        if ratio < min_ratio:
            failures.add(f"contrast {label} {a} on {b} is {ratio:.2f}:1, need {min_ratio}")

    check_secrets(ROOT, failures)

    if failures:
        print(f"FAIL ({len(failures)} issue(s)):")
        for msg in failures:
            print(f"  - {msg}")
        return 1
    print("PASS: starter vaults look consistent and well-formed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
