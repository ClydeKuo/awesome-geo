"""Validate the awesome-geo dataset. Usage: validate.py [--strict] [--data data]"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.geo_data import (  # noqa: E402
    LANGS, PRICING, REGIONS, TYPES, Dataset, all_paths, has_tracking_params,
    is_blank, leaf_paths, load_dataset, normalize_url,
)

# Keys every i18n.yaml must define.
REQUIRED_I18N_KEYS: list[str] = [
    "title", "tagline", "what_is_geo_title", "what_is_geo", "toc_title",
    "legend_title", "legend_colon", "legend_separator", "legend_free", "legend_freemium", "legend_paid",
    "legend_open_source", "contributing_title", "contributing_text",
    "license_title", "license_text",
]

DESC_LIMITS = {"en": 200, "es": 200, "de": 200, "zh-CN": 100, "ja": 100, "ko": 100}
KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


@dataclass
class Issue:
    level: Literal["error", "warning"]
    where: str
    message: str


def _check_translations(issues, where, values, strict, what):
    """en missing is always an error; other langs warn (lenient) or error (strict)."""
    values = values if isinstance(values, dict) else {}
    for lang in LANGS:
        v = values.get(lang)
        if not is_blank(v):
            continue
        level = "error" if (strict or lang == "en") else "warning"
        issues.append(Issue(level, where, f"missing {lang} {what}"))


def _walk(categories):
    for c in categories:
        yield c
        yield from _walk(c.children)


def validate(ds: Dataset, strict: bool) -> list[Issue]:
    issues: list[Issue] = []
    err = lambda w, m: issues.append(Issue("error", w, m))  # noqa: E731

    for c in _walk(ds.categories):
        _check_translations(issues, f"category {c.path}", c.title, strict, "title")
        if c.intro is not None:
            _check_translations(issues, f"category {c.path}", c.intro, strict, "intro")
        if c.depth > 1:
            err(f"category {c.path}", "categories may nest only one level")

    for key in REQUIRED_I18N_KEYS:
        if key not in ds.i18n:
            err("i18n", f"missing required key '{key}'")
    for key, values in ds.i18n.items():
        _check_translations(issues, f"i18n {key}", values, strict, "text")

    leaves = leaf_paths(ds.categories)
    known = all_paths(ds.categories)
    seen_ids: dict[str, str] = {}
    seen_urls: dict[str, str] = {}

    for r in ds.resources:
        where = f"{r.source_file}:{r.id or '?'}"
        if not r.id or not KEBAB.match(r.id):
            err(where, f"id '{r.id}' must be kebab-case")
        if r.id in seen_ids:
            err(where, f"duplicate id '{r.id}'")
        seen_ids.setdefault(r.id, where)

        if not r.name.strip():
            err(where, "missing name")
        if not r.url.strip():
            err(where, "missing url")
        else:
            if has_tracking_params(r.url):
                err(where, f"url has tracking parameters: {r.url}")
            norm = normalize_url(r.url)
            if norm in seen_urls:
                err(where, f"duplicate url {norm} (also {seen_urls[norm]})")
            seen_urls.setdefault(norm, where)

        if r.category not in known:
            err(where, f"unknown category '{r.category}'")
        else:
            if r.category not in leaves:
                err(where, f"category '{r.category}' is not a leaf category")
            if r.category.split("/")[0] != r.source_file:
                err(where, f"resource in file '{r.source_file}.yaml' but category is '{r.category}'")

        if r.type not in TYPES:
            err(where, f"invalid type '{r.type}'")
        if r.pricing not in PRICING:
            err(where, f"invalid pricing '{r.pricing}'")
        for region in r.regions:
            if region not in REGIONS:
                err(where, f"invalid regions entry '{region}'")
        if not isinstance(r.open_source, bool):
            err(where, "open_source must be a boolean")
        if r.year is not None and (isinstance(r.year, bool) or not isinstance(r.year, int)):
            err(where, "year must be an integer")

        for lang, v in r.desc.items():
            if lang not in LANGS:
                err(where, f"desc has unknown language key '{lang}'")
            elif not isinstance(v, str):
                err(where, f"desc '{lang}' must be a string")
        _check_translations(issues, where, r.desc, strict, "desc")
        for lang, limit in DESC_LIMITS.items():
            v = r.desc.get(lang)
            if isinstance(v, str) and len(v.strip()) > limit:
                err(where, f"{lang} desc is {len(v.strip())} chars (max {limit})")

    return issues


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--strict", action="store_true")
    p.add_argument("--data", default="data")
    args = p.parse_args(argv)
    issues = validate(load_dataset(Path(args.data)), strict=args.strict)
    for i in issues:
        print(f"{i.level.upper()}: {i.where}: {i.message}")
    errors = sum(i.level == "error" for i in issues)
    print(f"{errors} error(s), {len(issues) - errors} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
