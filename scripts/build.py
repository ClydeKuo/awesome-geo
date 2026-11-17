"""Generate the multi-language READMEs. Usage: build.py [--data data] [--out .]"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.geo_data import LANGS, Category, Dataset, Resource, load_dataset  # noqa: E402

README_FILES = {
    "en": "README.md",
    "zh-CN": "README.zh-CN.md",
    "ja": "README.ja.md",
    "ko": "README.ko.md",
    "es": "README.es.md",
    "de": "README.de.md",
}
LANG_NAMES = {
    "en": "English", "zh-CN": "简体中文", "ja": "日本語",
    "ko": "한국어", "es": "Español", "de": "Deutsch",
}
PRICING_EMOJI = {"free": "🆓", "freemium": "🪙", "paid": "💲"}
OPEN_SOURCE_EMOJI = "🔓"
BADGE = "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)"
TERMINAL_PUNCT = ".!?。！？"

_MD_SPECIAL = re.compile(r"([\\\[\]|`*_<>])")


def github_slug(text: str) -> str:
    kept = "".join(c for c in text.lower() if c.isalnum() or c in " -_")
    return kept.replace(" ", "-")


class SlugRegistry:
    """Mimics GitHub's anchor generation, including -1/-2 suffixes for duplicates."""

    def __init__(self) -> None:
        self._used: set[str] = set()
        self._counts: dict[str, int] = {}

    def slug(self, text: str) -> str:
        base = github_slug(text)
        candidate = base
        n = self._counts.get(base, 0)
        while candidate in self._used:
            n += 1
            candidate = f"{base}-{n}"
        self._counts[base] = n
        self._used.add(candidate)
        return candidate


def tr(values: dict | None, lang: str) -> str:
    """Text for lang, falling back to English when missing or blank."""
    values = values or {}
    for key in (lang, "en"):
        v = values.get(key)
        if isinstance(v, str) and v.strip():
            return v.strip()
    return ""


def _escape(text: str) -> str:
    return _MD_SPECIAL.sub(r"\\\1", " ".join(text.split()))


def _safe_url(url: str) -> str:
    return url.strip().replace(" ", "%20").replace("(", "%28").replace(")", "%29")


def render_item(r: Resource, lang: str) -> str:
    desc = _escape(tr(r.desc, lang))
    if desc and desc[-1] not in TERMINAL_PUNCT:
        desc += "。" if lang in ("zh-CN", "ja") else "."
    tags = [PRICING_EMOJI[r.pricing]] if r.pricing in PRICING_EMOJI else []
    if r.open_source:
        tags.append(OPEN_SOURCE_EMOJI)
    line = f"- [{_escape(r.name)}]({_safe_url(r.url)})"
    if tags:
        line += " " + " ".join(tags)
    if desc:
        line += f" - {desc}"
    if r.year is not None:
        line += f" ({r.year})"
    return line


def _sort_key(r: Resource):
    if r.type == "paper":
        return (0, -(r.year or 0), r.name.casefold(), r.id)
    return (1, 0, r.name.casefold(), r.id)


def _by_category(ds: Dataset) -> dict[str, list[Resource]]:
    out: dict[str, list[Resource]] = {}
    for r in ds.resources:
        out.setdefault(r.category, []).append(r)
    for items in out.values():
        items.sort(key=_sort_key)
    return out


def _non_empty(cat: Category, by_cat) -> bool:
    return bool(by_cat.get(cat.path)) or any(_non_empty(c, by_cat) for c in cat.children)


def render_readme(ds: Dataset, lang: str) -> str:
    t = lambda key: tr(ds.i18n.get(key), lang)  # noqa: E731
    by_cat = _by_category(ds)
    top = [c for c in ds.categories if _non_empty(c, by_cat)]

    # Headings in document order; the registry assigns anchors exactly as GitHub will.
    # awesome-lint requires the ToC to be the first section, titled "Contents" in English.
    reg = SlugRegistry()
    reg.slug(t("title"))
    reg.slug(t("toc_title"))
    toc: list[str] = []

    def toc_entry(indent: int, text: str) -> None:
        toc.append(f"{'  ' * indent}- [{text}](#{reg.slug(text)})")

    toc_entry(0, t("what_is_geo_title"))
    for c in top:
        toc_entry(0, tr(c.title, lang))
        for child in c.children:
            if _non_empty(child, by_cat):
                toc_entry(1, tr(child.title, lang))
    reg.slug(t("contributing_title"))  # not listed in the ToC, but still takes an anchor
    toc_entry(0, t("license_title"))

    switcher = " | ".join(
        f"**{LANG_NAMES[code]}**" if code == lang else f"[{LANG_NAMES[code]}]({README_FILES[code]})"
        for code in LANGS
    )
    # raw lookup: tr() strips whitespace, but the separator may carry a trailing space
    seps = ds.i18n.get("legend_separator") or {}
    sep = seps.get(lang) or seps.get("en") or ", "
    legend = (
        f"**{t('legend_title')}{t('legend_colon')}** "
        + sep.join([
            f"🆓 {t('legend_free')}", f"🪙 {t('legend_freemium')}",
            f"💲 {t('legend_paid')}", f"🔓 {t('legend_open_source')}",
        ])
    )

    out: list[str] = [
        f"# {t('title')} {BADGE}", "",
        switcher, "",
        f"> {t('tagline')}", "",
        f"## {t('toc_title')}", "",
        *toc, "",
        legend, "",
        f"## {t('what_is_geo_title')}", "",
        t("what_is_geo"), "",
    ]

    def section(cat: Category, level: int) -> None:
        out.extend([f"{'#' * level} {tr(cat.title, lang)}", ""])
        intro = tr(cat.intro, lang)
        if intro:
            out.extend([intro, ""])
        items = by_cat.get(cat.path, [])
        if items:
            out.extend([*(render_item(r, lang) for r in items), ""])
        for child in cat.children:
            if _non_empty(child, by_cat):
                section(child, level + 1)

    for c in top:
        section(c, 2)

    out.extend([
        f"## {t('contributing_title')}", "", t("contributing_text"), "",
        f"## {t('license_title')}", "", t("license_text"), "",
    ])
    return "\n".join(out).rstrip("\n") + "\n"


def build_all(ds: Dataset, out_dir: Path) -> list[Path]:
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    for lang in LANGS:
        path = out_dir / README_FILES[lang]
        path.write_text(render_readme(ds, lang), encoding="utf-8", newline="\n")
        paths.append(path)
    return paths


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--data", default="data")
    p.add_argument("--out", default=".")
    args = p.parse_args(argv)
    for path in build_all(load_dataset(Path(args.data)), Path(args.out)):
        print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
