import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

LANGS = ["en", "zh-CN", "ja", "ko", "es", "de"]


def full(text):
    return {lang: text for lang in LANGS}


REQUIRED_I18N_KEYS = [
    "title", "tagline", "what_is_geo_title", "what_is_geo", "toc_title",
    "legend_title", "legend_colon", "legend_separator", "legend_free", "legend_freemium", "legend_paid",
    "legend_open_source", "contributing_title", "contributing_text",
    "license_title", "license_text",
]
DEFAULT_I18N = {key: full(f"[{key}]") for key in REQUIRED_I18N_KEYS}
DEFAULT_I18N["title"] = full("Awesome GEO")
DEFAULT_I18N["toc_title"] = full("Contents")

DEFAULT_CATEGORIES = [
    {
        "id": "research",
        "title": full("Research"),
        "children": [{"id": "foundational", "title": full("Foundational")}],
    },
    {
        "id": "tools",
        "title": full("Tools"),
        "children": [{"id": "monitoring", "title": full("Monitoring")}],
    },
]

DEFAULT_RESOURCE = {
    "id": "geo-paper",
    "name": "GEO Paper",
    "url": "https://arxiv.org/abs/2311.09735",
    "category": "research/foundational",
    "type": "paper",
    "pricing": "free",
    "open_source": False,
    "regions": ["global"],
    "year": 2023,
    "desc": full("A paper."),
}


@pytest.fixture
def make_data(tmp_path):
    """Write a minimal valid data dir and return its path.

    resources: list of dicts merged over DEFAULT_RESOURCE (None -> one default
    resource). A "_file" key overrides the file stem the resource is written
    to (default: first segment of its category).
    categories: replaces DEFAULT_CATEGORIES.
    overrides (e.g. desc=...): merged into the default resource when
    `resources` is not given.
    """

    def _make(resources=None, categories=None, i18n=None, **overrides):
        if resources is None:
            resources = [overrides]
        elif overrides:
            raise TypeError("pass overrides either via resources or kwargs")
        data = tmp_path / "data"
        (data / "resources").mkdir(parents=True, exist_ok=True)
        (data / "config.yaml").write_text(
            "repo_owner: test-owner\nrepo_name: awesome-geo\n", encoding="utf-8"
        )
        cats = DEFAULT_CATEGORIES if categories is None else categories
        (data / "categories.yaml").write_text(
            yaml.safe_dump(cats, allow_unicode=True), encoding="utf-8"
        )
        (data / "i18n.yaml").write_text(
            yaml.safe_dump({**DEFAULT_I18N, **(i18n or {})}, allow_unicode=True),
            encoding="utf-8",
        )
        by_file = {}
        for r in resources:
            r = {**DEFAULT_RESOURCE, **r}
            stem = r.pop("_file", None) or r["category"].split("/")[0]
            by_file.setdefault(stem, []).append(r)
        for stem, items in by_file.items():
            (data / "resources" / f"{stem}.yaml").write_text(
                yaml.safe_dump(items, allow_unicode=True), encoding="utf-8"
            )
        return data

    return _make
