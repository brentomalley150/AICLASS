#!/usr/bin/env python3
"""
Build the BuildtheCrew PRD site from BuildtheCrew-PRD.md.

Usage:
    python docs/build.py [output_dir]

Reads:  docs/BuildtheCrew-PRD.md, docs/template.html
Writes: <output_dir>/index.html  (default: docs/)
"""
import re
import shutil
import sys
from pathlib import Path

import markdown

HERE = Path(__file__).resolve().parent
SRC_MD = HERE / "BuildtheCrew-PRD.md"
TEMPLATE = HERE / "template.html"

OUT_DIR = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_HTML = OUT_DIR / "index.html"


def slugify(value: str) -> str:
    """Stable, human-readable slug. Strips leading section numbers like '1. '."""
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"^\d+\.\s*", "", value).strip()
    value = value.lower()
    value = re.sub(r"[^\w\s-]", "", value)
    value = re.sub(r"[\s_-]+", "-", value).strip("-")
    return value or "section"


def extract_meta(text: str):
    """Pull title + Author/Date/Status from the top of the markdown."""
    title = "PRD"
    meta = {"Author": "", "Date": "", "Status": ""}
    for line in text.splitlines()[:20]:
        m = re.match(r"^#\s+(?:PRD:\s+)?(.+)$", line)
        if m and title == "PRD":
            title = m.group(1).strip()
        m = re.match(r"^\*\*(Author|Date|Status):\*\*\s+(.+)$", line)
        if m:
            meta[m.group(1)] = m.group(2).strip()
    return title, meta


def strip_meta_block(text: str) -> str:
    """Remove the title + bold Author/Date/Status lines + the leading '---' separator."""
    return re.sub(
        r"\A#\s+.+?\n(?:\*\*(?:Author|Date|Status):\*\*.*?\n)+\s*\n---\s*\n",
        "",
        text,
        count=1,
        flags=re.DOTALL,
    )


def render_markdown(body_md: str) -> str:
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])
    return md.convert(body_md)


def post_process_need(html: str) -> str:
    """`[NEED: ...]` (rendered as <code>) becomes a styled callout span."""
    return re.sub(
        r"<code>\[NEED:\s*(.*?)\]</code>",
        lambda m: f'<span class="need">NEED: {m.group(1)}</span>',
        html,
        flags=re.DOTALL,
    )


def post_process_checklists(html: str) -> str:
    """Convert <ul> blocks whose <li>s start with '[ ]' or '[x]' into a styled checklist."""
    def maybe_checklist(match: re.Match) -> str:
        inner = match.group(1)
        if not re.search(r"<li>\s*\[[ xX]\]", inner):
            return match.group(0)
        new_inner = re.sub(
            r"<li>\s*\[([ xX])\]\s*(.*?)</li>",
            lambda m: f'<li class="{"done" if m.group(1).lower() == "x" else ""}">{m.group(2)}</li>',
            inner,
            flags=re.DOTALL,
        )
        return f'<ul class="checklist">{new_inner}</ul>'

    return re.sub(r"<ul>(.*?)</ul>", maybe_checklist, html, flags=re.DOTALL)


def add_heading_ids(html: str) -> str:
    """Add stable id slugs to h2 and h3 headings."""
    def add_id(tag: str):
        def repl(match: re.Match) -> str:
            attrs = match.group(1) or ""
            text = match.group(2)
            if "id=" in attrs:
                return match.group(0)
            return f"<{tag}{attrs} id=\"{slugify(text)}\">{text}</{tag}>"
        return repl

    html = re.sub(r"<h2(\s[^>]*)?>(.*?)</h2>", add_id("h2"), html, flags=re.DOTALL)
    html = re.sub(r"<h3(\s[^>]*)?>(.*?)</h3>", add_id("h3"), html, flags=re.DOTALL)
    return html


def build_toc(html: str) -> str:
    items = []
    for m in re.finditer(r'<h2[^>]*id="([^"]+)"[^>]*>(.*?)</h2>', html, flags=re.DOTALL):
        sid = m.group(1)
        text = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        items.append(f'<li><a href="#{sid}">{text}</a></li>')
    if not items:
        return "<ol></ol>"
    return "<ol>\n  " + "\n  ".join(items) + "\n</ol>"


def main():
    raw = SRC_MD.read_text(encoding="utf-8")
    title, meta = extract_meta(raw)
    body_md = strip_meta_block(raw)

    html = render_markdown(body_md)
    html = post_process_need(html)
    html = post_process_checklists(html)
    html = add_heading_ids(html)
    toc_html = build_toc(html)

    template = TEMPLATE.read_text(encoding="utf-8")
    page = (
        template
        .replace("{{title}}", title)
        .replace("{{author}}", meta["Author"])
        .replace("{{date}}", meta["Date"])
        .replace("{{status}}", meta["Status"])
        .replace("{{toc}}", toc_html)
        .replace("{{content}}", html)
    )
    OUT_HTML.write_text(page, encoding="utf-8")
    print(f"Built {OUT_HTML}")

    # Also copy raw md + .nojekyll into the output dir so the deployed site is complete.
    if OUT_DIR != HERE:
        shutil.copy2(SRC_MD, OUT_DIR / SRC_MD.name)
        nojekyll = HERE / ".nojekyll"
        if nojekyll.exists():
            shutil.copy2(nojekyll, OUT_DIR / ".nojekyll")
        else:
            (OUT_DIR / ".nojekyll").touch()


if __name__ == "__main__":
    main()
