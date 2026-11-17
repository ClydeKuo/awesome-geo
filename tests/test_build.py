import pytest

from scripts.build import (
    README_FILES, SlugRegistry, build_all, github_slug, render_item, render_readme,
)
from scripts.geo_data import LANGS, Resource, load_dataset

from conftest import full


def res(**kw):
    base = dict(
        id="x", name="Tool", url="https://example.com/tool", category="tools/monitoring",
        type="tool", pricing="free", open_source=True, repo=None, regions=["global"],
        year=None, desc=full("Does a thing."), source_file="tools",
    )
    base.update(kw)
    return Resource(**base)


@pytest.fixture
def ds(make_data):
    return load_dataset(make_data())


def test_readme_files():
    assert list(README_FILES) == LANGS
    assert list(README_FILES.values()) == [
        "README.md", "README.zh-CN.md", "README.ja.md", "README.ko.md",
        "README.es.md", "README.de.md",
    ]


def test_render_item_format():
    r = res(name="GEO Paper", url="https://arxiv.org/abs/2311.09735", year=2023,
            desc={"en": "Introduces GEO."})
    assert render_item(r, "en") == "- [GEO Paper](https://arxiv.org/abs/2311.09735) 🆓 🔓 - Introduces GEO. (2023)"


def test_render_item_without_tags_or_year():
    r = res(pricing="n/a", open_source=False, desc={"en": "Plain"})
    assert render_item(r, "en") == "- [Tool](https://example.com/tool) - Plain."


def test_render_item_pricing_emojis():
    assert "🪙" in render_item(res(pricing="freemium", open_source=False), "en")
    assert "💲" in render_item(res(pricing="paid", open_source=False), "en")


def test_render_item_escapes_and_single_line():
    r = res(name="A [B] | C", desc={"en": "Line one\nline two [x]."})
    out = render_item(r, "en")
    assert "\n" not in out and r"A \[B\] \| C" in out
    assert "Line one line two" in out and r"\[x\]" in out


def test_render_item_url_with_parens():
    out = render_item(res(url="https://en.wikipedia.org/wiki/GEO_(x)"), "en")
    assert "(https://en.wikipedia.org/wiki/GEO_%28x%29)" in out


def test_github_slug():
    assert github_slug("Research Papers") == "research-papers"
    assert github_slug("Tools & Libraries") == "tools--libraries"
    assert github_slug("研究论文") == "研究论文"
    assert github_slug("AI 検索エンジン（地域別）") == "ai-検索エンジン地域別"


def test_slug_registry_duplicates():
    reg = SlugRegistry()
    assert [reg.slug("Global") for _ in range(3)] == ["global", "global-1", "global-2"]


def cats_with_empty():
    return [
        {"id": "research", "title": full("Research"),
         "children": [{"id": "foundational", "title": full("Foundational")}]},
        {"id": "tools", "title": full("Empty Cat"),
         "children": [{"id": "monitoring", "title": full("Empty Sub")}]},
    ]


def test_empty_categories_omitted(make_data):
    ds = load_dataset(make_data(categories=cats_with_empty()))
    md = render_readme(ds, "en")
    assert "Empty Cat" not in md and "Empty Sub" not in md
    assert "## Research" in md and "### Foundational" in md


def test_sorting_papers_by_year_desc_then_name(make_data):
    data = make_data(resources=[
        {"id": "a", "name": "Beta", "url": "https://a.com", "year": 2023},
        {"id": "b", "name": "alpha", "url": "https://b.com", "year": 2023},
        {"id": "c", "name": "Zed", "url": "https://c.com", "year": 2024},
        {"id": "d", "name": "Old", "url": "https://d.com", "year": 2020},
    ])
    md = render_readme(load_dataset(data), "en")
    order = [md.index(f"[{n}]") for n in ("Zed", "alpha", "Beta", "Old")]
    assert order == sorted(order)


def test_sorting_others_case_insensitive(make_data):
    data = make_data(resources=[
        {"id": "a", "name": "banana", "url": "https://a.com", "type": "tool", "category": "tools/monitoring"},
        {"id": "b", "name": "Apple", "url": "https://b.com", "type": "tool", "category": "tools/monitoring"},
        {"id": "c", "name": "cherry", "url": "https://c.com", "type": "tool", "category": "tools/monitoring"},
    ])
    md = render_readme(load_dataset(data), "en")
    order = [md.index(f"[{n}]") for n in ("Apple", "banana", "cherry")]
    assert order == sorted(order)


def test_language_switcher_current_bold(ds):
    md = render_readme(ds, "ja")
    assert "**日本語**" in md and "[English](README.md)" in md and "[简体中文](README.zh-CN.md)" in md
    assert "[日本語]" not in md


def test_structure_and_trailing_newline(make_data):
    i18n = {"legend_free": full("free"), "legend_freemium": full("freemium"),
            "legend_paid": full("paid"), "legend_open_source": full("open source")}
    md = render_readme(load_dataset(make_data(i18n=i18n)), "en")
    assert md.startswith("# Awesome GEO [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)\n")
    assert md.endswith("\n") and not md.endswith("\n\n")
    assert "🆓 free" in md and "🪙 freemium" in md and "💲 paid" in md and "🔓 open source" in md


def test_intro_rendered(make_data):
    cats = [{"id": "research", "title": full("Research"), "intro": full("Intro text."),
             "children": [{"id": "foundational", "title": full("Foundational")}]},
            {"id": "tools", "title": full("Tools"),
             "children": [{"id": "monitoring", "title": full("Monitoring")}]}]
    md = render_readme(load_dataset(make_data(categories=cats)), "en")
    assert "## Research\n\nIntro text.\n" in md


def toc_and_headings(md):
    import re
    lines = md.splitlines()
    anchors = [m.group(1) for ln in lines for m in [re.match(r"\s*- \[.*\]\(#(.+)\)$", ln)] if m]
    reg = SlugRegistry()
    slugs = {reg.slug(re.sub(r"\[!\[.*", "", ln.lstrip("# ")).strip()) for ln in lines if ln.startswith("#")}
    return anchors, slugs


def test_toc_links_match_headings(make_data):
    cats = [{"id": "research", "title": full("Global"),
             "children": [{"id": "foundational", "title": full("Global")}]},
            {"id": "tools", "title": full("研究 & 論文"),
             "children": [{"id": "monitoring", "title": full("Global")}]}]
    data = make_data(resources=[
        {"id": "a", "url": "https://a.com"},
        {"id": "b", "url": "https://b.com", "category": "tools/monitoring", "type": "tool"},
    ], categories=cats)
    md = render_readme(load_dataset(data), "en")
    anchors, slugs = toc_and_headings(md)
    assert "global-1" in anchors and "global-2" in anchors
    assert anchors and set(anchors) <= slugs


def test_build_is_deterministic(ds, tmp_path):
    a = [p.read_text(encoding="utf-8") for p in build_all(ds, tmp_path)]
    b = [p.read_text(encoding="utf-8") for p in build_all(ds, tmp_path)]
    assert a == b and len(a) == 6
    assert sorted(p.name for p in tmp_path.glob("README*.md")) == sorted(README_FILES.values())


def test_missing_translation_falls_back_to_en(make_data):
    data = make_data(desc={"en": "English only.", "ja": "  "})
    ds = load_dataset(data)
    md = render_readme(ds, "de")
    assert "English only." in md
    assert "English only." in render_readme(ds, "ja")
