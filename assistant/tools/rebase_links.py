#!/usr/bin/env python3
"""One-time link rebasing from the pre-restructure tree. No network or LLM calls."""
import os
import re
import subprocess
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

BASE = "a6e0b9b4f3df32cae9204adc0f09f45750c7365b"
ROOT = Path(__file__).resolve().parents[2]
SKIP = {".gitignore", "README.md", "architecture/dual_loop_v1.0.1/README.md",
        "visualization/build_engineering_package.py",
        ".github/workflows/build-engineering-visualization.yml"}
EXTENSIONS = {".md", ".html", ".css", ".txt", ".csv"}
SPECIAL = {
    "AGENTS.md": "assistant/AGENTS.md",
    "RESEARCH_PLAN.md": "assistant/RESEARCH_PLAN.md",
    "RESEARCH_WRITING_STANDARD.md": "assistant/RESEARCH_WRITING_STANDARD.md",
    "CHANGELOG.md": "assistant/CHANGELOG.md",
    "JXWORK_START_HERE.md": "assistant/JXWORK_START_HERE.md",
    "architecture/dual_loop_v1.0.1/README.md": "shared/architecture/V1.0.1/README.md",
    "architecture/dual_loop_v1.0.1/DESIGN_HANDOFF_2026-10-28.md": "assistant/handoffs/DESIGN_HANDOFF_2026-10-28.md",
    "architecture/research_loop_inputs_draft/README.md": "shared/architecture/V1.0.1/RESEARCH_LOOP.md",
    "architecture/research_loop_inputs_draft/RESEARCH_INPUT_PROTOCOL_V1.md": "shared/architecture/V1.0.1/RESEARCH_INPUT_PROTOCOL_V1.md",
    "architecture/research_loop_inputs_draft/DAILY_ADMISSION_AGENT_V0.md": "assistant/handoffs/DAILY_ADMISSION_AGENT_V0.md",
}

def mapped(path):
    if path in SPECIAL:
        return SPECIAL[path]
    if path.startswith(("papers/", "knowledge/", "synthesis/", "ai_trains_ai/",
                        "intraday_to_daily/", "evaluation/")):
        return "shared/" + path
    if path.startswith(("visualization/", "technical_reading/")):
        return "presentation/" + path
    return path

def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)

old_paths = set(git("ls-tree", "-r", "--name-only", BASE).decode().splitlines())
old_dirs = set()
for path in old_paths:
    parts = path.split("/")
    old_dirs.update("/".join(parts[:k]) for k in range(1, len(parts)))

def rebase_link(url, src, dst):
    if url.startswith(("#", "//")) or re.match(r"^(mailto:|data:|javascript:|tel:)", url, re.I):
        return url
    match = re.match(r"^https://github\.com/epshoron/JXwork/(blob|tree)/main/([^?#]+)(.*)$", url)
    if match:
        kind, raw, suffix = match.groups()
        old = unquote(raw)
        if old in old_paths or old in old_dirs:
            return "https://github.com/epshoron/JXwork/" + kind + "/main/" + quote(mapped(old), safe="/.-_") + suffix
        return url
    if re.match(r"^[a-z][a-z0-9+.-]*:", url, re.I) or url.startswith("/"):
        return url
    ref = urlsplit(url)
    if not ref.path:
        return url
    old = os.path.normpath(os.path.join(os.path.dirname(src), unquote(ref.path))).replace("\\", "/")
    if old not in old_paths and old not in old_dirs:
        return url
    newer = mapped(old)
    # A shared-only archive should not need assistant files to resolve.
    if dst.startswith("shared/") and newer.startswith("assistant/"):
        output = "https://github.com/epshoron/JXwork/blob/main/" + quote(newer, safe="/.-_")
    else:
        output = quote(os.path.relpath(newer, os.path.dirname(dst) or ".").replace("\\", "/"), safe="/.-_")
    if ref.query:
        output += "?" + ref.query
    if ref.fragment:
        output += "#" + ref.fragment
    return output

def rewrite(text, src, dst):
    text = re.sub(r"(\]\()([^\s)]+)", lambda m: m.group(1) + rebase_link(m.group(2), src, dst), text)
    text = re.sub(r"(\b(?:href|src)=[\"'])([^\"']+)([\"'])",
                  lambda m: m.group(1) + rebase_link(m.group(2), src, dst) + m.group(3), text, flags=re.I)
    text = re.sub(r"(url\(\s*[\"']?)([^)\"']+)([\"']?\s*\))",
                  lambda m: m.group(1) + rebase_link(m.group(2), src, dst) + m.group(3), text, flags=re.I)
    text = re.sub(r"https://github\.com/epshoron/JXwork/(?:blob|tree)/main/[^\s)\"'>]+",
                  lambda m: rebase_link(m.group(0), src, dst), text)
    return text

modified = []
skipped = []
for source in sorted(old_paths):
    if source in SKIP or Path(source).suffix.lower() not in EXTENSIONS:
        continue
    target = mapped(source)
    destfile = ROOT / target
    if not destfile.is_file():
        continue
    old_data = git("show", BASE + ":" + source).decode("utf-8")
    current = destfile.read_text(encoding="utf-8")
    # Hand-edited V1.0.1 files retain new content; rebase its old relative links.
    allowed_changed = source in ("architecture/research_loop_inputs_draft/README.md",
                                 "architecture/research_loop_inputs_draft/RESEARCH_INPUT_PROTOCOL_V1.md")
    if current != old_data and not allowed_changed:
        skipped.append(target)
        continue
    updated = rewrite(current, source, target)
    if updated != current:
        destfile.write_text(updated, encoding="utf-8")
        modified.append(target)

# Maintain an explicit current handoff for the research LLM rather than stale old pointer.
pointer = ROOT / "assistant/JXWORK_START_HERE.md"
pointer.write_text("""# JXwork｜研究维护 Agent 接手入口（2026-10-29）

**本文件只服务于 ChatGPT / 文献研究维护 Agent，不是公司云端执行指令。**

1. 先读 [AGENTS.md](AGENTS.md)、[研究写作标准](RESEARCH_WRITING_STANDARD.md)、[研究计划](RESEARCH_PLAN.md)。
2. A：[论文 P Index](../shared/papers/INDEX.md) / [机制 D Index](../shared/knowledge/DELTA_INDEX.md)。
3. B：[论文 T Index](../shared/ai_trains_ai/papers/INDEX.md) / [机制 TD Index](../shared/ai_trains_ai/knowledge/DELTA_INDEX.md)。
4. C：[学术论文 C Index](../shared/intraday_to_daily/papers/INDEX.md) / [券商研报 CR Index](../shared/intraday_to_daily/reports/INDEX.md)。
5. 已确认的唯一系统架构：[V1.0.1](../shared/architecture/V1.0.1/README.md)。最新 Research Loop v9 代替旧研究侧方案；Meta Loop 还没有启动。
6. 更新记录见 [CHANGELOG.md](CHANGELOG.md)。

论文骨架须有原文证据；创新/特化不足/Delta 仍需研究者逐项审批、严格去重，同回合维护对应 Index。公司内部资料和密钥不得进入本仓库。
""", encoding="utf-8")
modified.append("assistant/JXWORK_START_HERE.md")
agents = ROOT / "assistant/AGENTS.md"
agent_text = agents.read_text(encoding="utf-8")
if "2026-10-29 目录重构声明" not in agent_text:
    agents.write_text("> **2026-10-29 目录重构声明：本文件只约束研究资料维护 Agent，云端执行 Agent 不应继承本文件。** 旧研究根路径现统一位于 shared/；最新拍板设计为 shared/architecture/V1.0.1/。历史代码路径示例按 [目录迁移说明](README.md) 解释。\n\n" + agent_text, encoding="utf-8")
    modified.append("assistant/AGENTS.md")
changelog = ROOT / "assistant/CHANGELOG.md"
ch = changelog.read_text(encoding="utf-8")
if "2026-10-29 · 三目录重构" not in ch:
    first = ch.find("\n")
    entry = """

## 2026-10-29 · 三目录重构与现行 V1.0.1 架构确认

- 研究者明确批准 shared（公司云端可用研究资料）/ assistant（研究 LLM 协作规则）/ presentation（本地展示）三类分离；原 A/B/C 编号与文件保留。
- 最新 Research Loop v9 双流程图取代旧双 Loop 研究侧草图，成为 shared/architecture/V1.0.1/ 的当前拍板架构；Meta Loop 尚未启动。
- 系统仍未实现或验证：模型/API 数量、检索、遮蔽比例、Daily 准入数值阈值及正式因子池晋级规则仍待研究，Evaluator V1 不变。
- GitHub Actions 新增 shared 单独 ZIP 工件；移动脚本与文档路径，保留二进制原始资料及 Git 历史。

"""
    changelog.write_text(ch[:first+1] + entry + ch[first+1:], encoding="utf-8")
    modified.append("assistant/CHANGELOG.md")
print("Rebased:", len(modified), "files. Unchanged/manual skipped:", len(skipped))
for path in modified:
    print("REBASED", path)
if skipped:
    print("SKIPPED", ", ".join(skipped[:15]))
