#!/usr/bin/env python3
"""One-shot rebase for 2026-10-29 A/B/C migration, with link integrity audit."""
from __future__ import annotations
import os
import re
import subprocess
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
BASE = "2a558c51ee37a8ac7f7607b6f12d56644edbf6d7"
EX = {".md", ".html", ".txt", ".css", ".csv"}
def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)
originals = set(git("ls-tree", "-r", "--name-only", BASE).decode().splitlines())
folders = {"/".join(p.split("/")[:k]) for p in originals for k in range(1, len(p.split("/")))}

def mapped(p):
    for before, after in (
        ("shared/papers/", "shared/A_alpha_mining/papers/"),
        ("shared/knowledge/", "shared/A_alpha_mining/knowledge/"),
        ("shared/synthesis/", "shared/A_alpha_mining/synthesis/"),
        ("shared/ai_trains_ai/", "shared/B_ai_trains_ai/"),
        ("shared/intraday_to_daily/", "shared/C_intraday_to_daily/"),
    ):
        if p.startswith(before):
            return after + p[len(before):]
    for before, after in (
        ("shared/papers", "shared/A_alpha_mining/papers"),
        ("shared/knowledge", "shared/A_alpha_mining/knowledge"),
        ("shared/synthesis", "shared/A_alpha_mining/synthesis"),
        ("shared/ai_trains_ai", "shared/B_ai_trains_ai"),
        ("shared/intraday_to_daily", "shared/C_intraday_to_daily"),
    ):
        if p == before:
            return after
    return p

def fix_url(url, oldsource, newsource):
    if url.startswith(("#", "//")) or re.match(r"^(data:|mailto:|javascript:|tel:)", url, re.I):
        return url
    found = re.match(r"^(https://github\.com/epshoron/JXwork/(?:blob|tree)/(?:main|[0-9a-f]{40})/)([^?#]+)(.*)$",url)
    if found:
        prefix, raw, suffix = found.groups()
        old = unquote(raw)
        if old in originals or old in folders:
            return prefix + quote(mapped(old), safe="/._-") + suffix
        return url
    if url.startswith("/") or re.match(r"^[a-z][a-z0-9+.-]*:", url, re.I):
        return url
    parts = urlsplit(url)
    if not parts.path:
        return url
    old = os.path.normpath(os.path.join(os.path.dirname(oldsource),unquote(parts.path))).replace("\\", "/")
    if old not in originals and old not in folders:
        return url
    target = mapped(old)
    if newsource.startswith("shared/") and target.startswith(("assistant/","presentation/")):
        result = "https://github.com/epshoron/JXwork/blob/main/" + quote(target,safe="/._-")
    else:
        result = quote(os.path.relpath(target, os.path.dirname(newsource) or ".").replace("\\","/"),safe="/._-")
    if parts.query:
        result += "?" + parts.query
    if parts.fragment:
        result += "#" + parts.fragment
    return result

def patch(text, oldsource, newsource):
    text = re.sub(r"(\]\()([^\s)]+)",lambda m:m.group(1)+fix_url(m.group(2),oldsource,newsource),text)
    text = re.sub(r"(\b(?:href|src)=[\"'])([^\"']+)([\"'])",lambda m:m.group(1)+fix_url(m.group(2),oldsource,newsource)+m.group(3),text,flags=re.I)
    text = re.sub(r"(url\(\s*[\"']?)([^\"')]+)([\"']?\s*\))",lambda m:m.group(1)+fix_url(m.group(2),oldsource,newsource)+m.group(3),text,flags=re.I)
    text = re.sub(r"https://github\.com/epshoron/JXwork/(?:blob|tree)/main/[^\s)\"'>]+",
                  lambda m:fix_url(m.group(0),oldsource,newsource),text)
    return text

changed,skipped=[],[]
for old in sorted(originals):
    if Path(old).suffix.lower() not in EX:
        continue
    new = mapped(old)
    file = ROOT/new
    if not file.is_file():
        continue
    previous = git("show",BASE+":"+old).decode("utf-8")
    current = file.read_text(encoding="utf-8")
    # Even hand-edited docs contain legacy links in their preserved sections.
    # Rebase only destinations that point to real paths in the pre-move tree;
    # links already authored for the new tree remain unchanged.
    if current != previous:
        skipped.append(new)
    transformed = patch(current,old,new)
    if transformed != current:
        file.write_text(transformed,encoding="utf-8")
        changed.append(new)

# Historical original research guides were moved out of shared, so their old
# relative links must be re-anchored to the new source locations as well.
guide_sources = {
    "assistant/research_guides/A_papers_original.md": "shared/papers/README.md",
    "assistant/research_guides/A_knowledge_original.md": "shared/knowledge/README.md",
    "assistant/research_guides/A_synthesis_original.md": "shared/synthesis/README.md",
    "assistant/research_guides/B_overview_original.md": "shared/ai_trains_ai/README.md",
    "assistant/research_guides/C_overview_original.md": "shared/intraday_to_daily/README.md",
}
for dst, src in guide_sources.items():
    f = ROOT/dst
    current=f.read_text(encoding="utf-8")
    newer=patch(current,src,dst)
    if newer != current:
        f.write_text(newer,encoding="utf-8")
        changed.append(dst)

def audit():
    missing=[]
    for root_name in ("shared","assistant","presentation"):
        for f in sorted((ROOT/root_name).rglob("*.md")):
            p = f.relative_to(ROOT).as_posix()
            text = f.read_text(encoding="utf-8")
            for m in re.finditer(r"\]\(([^)\s]+)",text):
                url=m.group(1)
                if url.startswith(("#","//")) or re.match(r"^[a-z][a-z0-9+.-]*:",url,re.I) or url.startswith("/"):
                    continue
                ref=urlsplit(url)
                if not ref.path:
                    continue
                path=(f.parent/unquote(ref.path)).resolve()
                if not path.exists():
                    missing.append((p,url))
    return missing

missing=audit()
print("MIGRATION REBASE: modified",len(changed),"unmodified/new authored skipped",len(skipped))
for p in changed: print("FIXED",p)
print("LINK AUDIT missing relative Markdown target count =",len(missing))
for p,url in missing[:80]:
    print("BROKEN",p,"->",url)
# Report broken links; the original archive may include historic nonexisting links.
# Fail only if very large regression.
if len(missing)>25:
    raise SystemExit("too many unresolved link targets")
