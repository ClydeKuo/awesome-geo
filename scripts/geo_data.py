"""Data model, loading and URL normalization for awesome-geo."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

import yaml

LANGS = ["en", "zh-CN", "ja", "ko", "es", "de"]
TYPES = {
    "paper", "article", "guide", "tool", "dataset", "benchmark", "engine",
    "spec", "community", "course", "video", "podcast", "newsletter",
    "case-study", "list",
}
PRICING = {"free", "freemium", "paid", "n/a"}
REGIONS = {"global", "us", "uk", "eu", "de", "fr", "es", "latam", "cn", "jp", "kr", "in", "ru"}

TRACKING_PARAMS = {"ref", "fbclid", "gclid"}


@dataclass
class Category:
    id: str
    path: str
    title: dict[str, str]
    intro: dict[str, str] | None
    children: list["Category"] = field(default_factory=list)
    depth: int = 0


@dataclass
class Resource:
    id: str
    name: str
    url: str
    category: str
    type: str
    pricing: str
    open_source: bool
    repo: str | None
    regions: list[str]
    year: int | None
    desc: dict[str, str]
    source_file: str


@dataclass
class Dataset:
    config: dict
    categories: list[Category]
    i18n: dict[str, dict[str, str]]
    resources: list[Resource]


def is_blank(s: str | None) -> bool:
    """True if s is missing, not a string, or whitespace-only."""
    return not isinstance(s, str) or not s.strip()


def _is_tracking(key: str) -> bool:
    k = key.lower()
    return k.startswith("utm_") or k in TRACKING_PARAMS


def has_tracking_params(url: str) -> bool:
    return any(_is_tracking(k) for k, _ in parse_qsl(urlsplit(url).query, keep_blank_values=True))


def normalize_url(url: str) -> str:
    parts = urlsplit(url.strip())
    host = parts.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    path = parts.path.rstrip("/")
    query = sorted(
        (k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True) if not _is_tracking(k)
    )
    return urlunsplit((parts.scheme.lower(), host, path, urlencode(query), ""))


def _build_categories(items, parent_path: str = "", depth: int = 0) -> list[Category]:
    out = []
    for item in items or []:
        path = f"{parent_path}/{item['id']}" if parent_path else str(item["id"])
        out.append(Category(
            id=str(item["id"]),
            path=path,
            title=dict(item.get("title") or {}),
            intro=dict(item["intro"]) if item.get("intro") else None,
            children=_build_categories(item.get("children"), path, depth + 1),
            depth=depth,
        ))
    return out


def leaf_paths(categories: list[Category]) -> set[str]:
    out: set[str] = set()
    for c in categories:
        if c.children:
            out |= leaf_paths(c.children)
        else:
            out.add(c.path)
    return out


def all_paths(categories: list[Category]) -> set[str]:
    out: set[str] = set()
    for c in categories:
        out.add(c.path)
        out |= all_paths(c.children)
    return out


def _load_yaml(path: Path):
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_dataset(data_dir: Path) -> Dataset:
    data_dir = Path(data_dir)
    config = _load_yaml(data_dir / "config.yaml") or {}
    categories = _build_categories(_load_yaml(data_dir / "categories.yaml"))
    i18n = _load_yaml(data_dir / "i18n.yaml") or {}
    resources: list[Resource] = []
    for f in sorted((data_dir / "resources").glob("*.yaml")):
        for r in _load_yaml(f) or []:
            resources.append(Resource(
                id=str(r.get("id", "")),
                name=str(r.get("name", "")),
                url=str(r.get("url", "")),
                category=str(r.get("category", "")),
                type=str(r.get("type", "")),
                pricing=str(r.get("pricing", "")),
                open_source=r.get("open_source", False),
                repo=r.get("repo"),
                regions=list(r.get("regions") or []),
                year=r.get("year"),
                desc=dict(r.get("desc") or {}),
                source_file=f.stem,
            ))
    return Dataset(config=config, categories=categories, i18n=i18n, resources=resources)
