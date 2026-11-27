/**
 * Run the bundled Archaeological Tomb Parser against the synthetic sample
 * in both starter vaults. This is the same autoExtract() path the Obsidian
 * command "Parse archaeological tombs" uses.
 */
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { TombParser } from "./vendor/tomb_parser.ts";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const sampleRel = join("Inbox", "示例墓葬文本.md");
const variants = ["zh-Hans", "zh-Hant"];

let failed = 0;
for (const variant of variants) {
  const path = join(root, "vault", variant, sampleRel);
  const text = readFileSync(path, "utf8");
  const parser = new TombParser("示例墓葬文本", text);
  const count = parser.autoExtract();
  const result = parser.toJSON();
  const tomb = result.墓葬列表[0];
  const problems: string[] = [];
  if (count !== 1) problems.push(`expected 1 tomb, got ${count}`);
  if (!tomb) {
    problems.push("no tomb in result");
  } else {
    if (tomb.墓葬编号 !== "M1") problems.push(`墓葬编号=${tomb.墓葬编号}`);
    if (tomb.墓葬形制 !== "土坑竖穴墓") problems.push(`墓葬形制=${tomb.墓葬形制}`);
    if (tomb.墓口长 !== 2.5) problems.push(`墓口长=${tomb.墓口长}`);
    if (tomb.墓口宽 !== 1.2) problems.push(`墓口宽=${tomb.墓口宽}`);
    if (tomb.墓深 !== 3.0) problems.push(`墓深=${tomb.墓深}`);
  }
  if (problems.length) {
    failed += 1;
    console.error(`FAIL ${variant}: ${problems.join("; ")}`);
  } else {
    console.log(`PASS ${variant}: extracted M1 土坑竖穴墓 2.5 x 1.2 x 3.0 m`);
  }
}

if (failed) {
  process.exit(1);
}
