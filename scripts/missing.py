"""List resources with missing translations. Usage: missing.py [--lang ja] [--format text|yaml]"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.geo_data import LANGS, Dataset, is_blank, load_dataset  # noqa: E402


def find_missing(ds: Dataset, lang: str | None = None) -> dict[str, list[str]]:
    """Map resource id -> missing langs (absent or blank), sorted by id."""
    langs = [lang] if lang else LANGS
    out: dict[str, list[str]] = {}
    for r in sorted(ds.resources, key=lambda r: r.id):
        miss = [l for l in langs if is_blank(r.desc.get(l))]
        if miss:
            out[r.id] = miss
    return out


def render_yaml(ds: Dataset, missing: dict[str, list[str]]) -> str:
    by_id = {r.id: r for r in ds.resources}
    items = []
    for rid, langs in missing.items():
        r = by_id[rid]
        desc = {"en": r.desc.get("en") or ""}
        desc.update({l: "" for l in langs if l != "en"})
        items.append({"id": r.id, "name": r.name, "url": r.url, "desc": desc})
    return yaml.safe_dump(items, allow_unicode=True, sort_keys=False)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--lang", choices=LANGS)
    p.add_argument("--format", choices=["text", "yaml"], default="text")
    p.add_argument("--data", default="data")
    args = p.parse_args(argv)
    ds = load_dataset(Path(args.data))
    missing = find_missing(ds, args.lang)
    if args.format == "yaml":
        if missing:
            sys.stdout.write(render_yaml(ds, missing))
    else:
        for rid, langs in missing.items():
            print(f"{rid}: {', '.join(langs)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
