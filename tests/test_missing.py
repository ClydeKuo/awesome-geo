import yaml

from scripts.geo_data import is_blank, load_dataset
from scripts.missing import find_missing, main


def _desc(**kw):
    d = {"en": "A.", "zh-CN": "甲", "ja": "あ", "ko": "가", "es": "A", "de": "A"}
    d.update(kw)
    return {k: v for k, v in d.items() if v is not None}


def test_is_blank():
    assert is_blank(None) and is_blank("") and is_blank("  \n")
    assert not is_blank("x")


def test_find_missing_lists_blank_and_absent(make_data):
    d = make_data(desc=_desc(ja=None, ko="  "))
    assert find_missing(load_dataset(d)) == {"geo-paper": ["ja", "ko"]}


def test_find_missing_complete_is_empty(make_data):
    assert find_missing(load_dataset(make_data(desc=_desc()))) == {}


def test_lang_filter(make_data, capsys):
    d = make_data(desc=_desc(ja=None, ko="  "))
    assert find_missing(load_dataset(d), lang="ja") == {"geo-paper": ["ja"]}
    assert find_missing(load_dataset(d), lang="de") == {}
    assert main(["--data", str(d), "--lang", "ko"]) == 0
    assert capsys.readouterr().out.strip() == "geo-paper: ko"


def test_sorted_by_id_and_text_format(make_data, capsys):
    d = make_data(resources=[
        {"id": "b-res", "url": "https://b.example", "desc": _desc(ja=None, ko="")},
        {"id": "a-res", "url": "https://a.example", "desc": _desc(de=" ")},
    ])
    assert list(find_missing(load_dataset(d))) == ["a-res", "b-res"]
    main(["--data", str(d)])
    assert capsys.readouterr().out.splitlines() == ["a-res: de", "b-res: ja, ko"]


def test_yaml_format(make_data, capsys):
    d = make_data(name="名称", desc=_desc(ja=None, ko="  "))
    main(["--data", str(d), "--format", "yaml"])
    out = capsys.readouterr().out
    assert "名称" in out
    loaded = yaml.safe_load(out)
    assert loaded == [{
        "id": "geo-paper", "name": "名称", "url": "https://arxiv.org/abs/2311.09735",
        "desc": {"en": "A.", "ja": "", "ko": ""},
    }]
    assert list(loaded[0]) == ["id", "name", "url", "desc"]
