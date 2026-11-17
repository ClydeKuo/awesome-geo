from scripts.geo_data import load_dataset, normalize_url, has_tracking_params, leaf_paths
from scripts.validate import validate

from conftest import full


def msgs(issues, level=None):
    return [i.message for i in issues if level is None or i.level == level]


def run(data, strict=True):
    return validate(load_dataset(data), strict=strict)


def test_normalize_url_equivalents():
    a = normalize_url("https://www.Example.com/a/")
    assert a == normalize_url("https://example.com/a") == normalize_url("https://example.com/a?utm_source=x#top")


def test_normalize_url_sorts_query_and_drops_tracking():
    assert normalize_url("https://x.com/a?b=2&a=1&ref=z&gclid=1") == normalize_url("https://x.com/a?a=1&b=2")
    assert has_tracking_params("https://x.com/a?fbclid=1")
    assert not has_tracking_params("https://x.com/a?a=1")


def test_leaf_paths(make_data):
    ds = load_dataset(make_data())
    assert leaf_paths(ds.categories) == {"research/foundational", "tools/monitoring"}


def test_valid_dataset_has_no_issues(make_data):
    assert run(make_data()) == []


def test_duplicate_normalized_url_is_error(make_data):
    data = make_data(resources=[
        {"id": "a", "url": "https://www.x.com/a/"},
        {"id": "b", "url": "https://x.com/a"},
    ])
    errs = [i for i in run(data) if i.level == "error"]
    assert len(errs) == 1 and "duplicate url" in errs[0].message


def test_duplicate_id_is_error(make_data):
    data = make_data(resources=[
        {"id": "a", "url": "https://x.com/1"},
        {"id": "a", "url": "https://x.com/2"},
    ])
    errs = run(data)
    assert len(errs) == 1 and "duplicate id" in errs[0].message


def test_tracking_param_is_error(make_data):
    errs = run(make_data(url="https://x.com/a?utm_source=x"))
    assert len(errs) == 1 and "tracking" in errs[0].message


def test_utm_variant_is_duplicate_and_tracking(make_data):
    data = make_data(resources=[
        {"id": "a", "url": "https://x.com/a"},
        {"id": "b", "url": "https://x.com/a?utm_source=y"},
    ])
    m = msgs(run(data))
    assert any("duplicate url" in x for x in m) and any("tracking" in x for x in m)


def test_unknown_category_and_non_leaf_category_error(make_data):
    data = make_data(resources=[
        {"id": "a", "url": "https://x.com/1", "category": "nope/x", "_file": "research"},
        {"id": "b", "url": "https://x.com/2", "category": "research"},
    ])
    errs = run(data)
    assert len(errs) == 2
    assert sum("nope/x" in i.message for i in errs) == 1
    assert sum("not a leaf" in i.message for i in errs) == 1


def test_resource_in_wrong_file_is_error(make_data):
    errs = run(make_data(category="tools/monitoring", _file="research"))
    assert len(errs) == 1 and "file" in errs[0].message


def test_enum_fields(make_data):
    for field, value in [("type", "blog"), ("pricing", "cheap"), ("regions", ["mars"])]:
        errs = run(make_data(**{field: value}))
        assert len(errs) == 1 and field in errs[0].message, field


def test_missing_translation_lenient_warns_strict_errors(make_data):
    data = make_data(desc={"en": "A paper.", "zh-CN": "   ", "ja": "x", "ko": "x", "es": "x", "de": "x"})
    assert {i.level for i in run(data, strict=False)} == {"warning"}
    strict = run(data, strict=True)
    assert strict and all(i.level == "error" for i in strict)


def test_missing_en_is_error_even_lenient(make_data):
    desc = full("x")
    desc["en"] = "  "
    issues = run(make_data(desc=desc), strict=False)
    assert [i.level for i in issues] == ["error"]


def test_desc_length_limits(make_data):
    bad = {**full("x"), "en": "a" * 201, "zh-CN": "字" * 101}
    assert len(run(make_data(desc=bad), strict=False)) == 2
    ok = {**full("x"), "en": "a" * 200, "zh-CN": "字" * 100}
    assert run(make_data(desc=ok)) == []


def test_desc_length_is_measured_after_strip(make_data):
    ok = {**full("x"), "en": "  " + "a" * 200 + "  "}
    assert run(make_data(desc=ok)) == []


def test_category_title_missing_lang(make_data):
    cats = [{"id": "research", "title": {k: "R" for k in ["en", "zh-CN", "ja", "es", "de"]},
             "children": [{"id": "foundational", "title": full("F")}]},
            {"id": "tools", "title": full("T"), "children": [{"id": "monitoring", "title": full("M")}]}]
    data = make_data(categories=cats)
    assert {i.level for i in run(data, strict=True)} == {"error"}
    assert {i.level for i in run(data, strict=False)} == {"warning"}


def test_category_title_missing_en_is_error_lenient(make_data):
    cats = [{"id": "research", "title": {"ja": "R"},
             "children": [{"id": "foundational", "title": full("F")}]},
            {"id": "tools", "title": full("T"), "children": [{"id": "monitoring", "title": full("M")}]}]
    assert "error" in {i.level for i in run(make_data(categories=cats), strict=False)}


def test_i18n_missing_lang(make_data):
    data = make_data(i18n={"contents": {"en": "Contents", "ja": "目次"}})
    assert {i.level for i in run(data, strict=True)} == {"error"}
    assert {i.level for i in run(data, strict=False)} == {"warning"}


def test_i18n_required_keys(make_data, monkeypatch):
    import scripts.validate as v
    monkeypatch.setattr(v, "REQUIRED_I18N_KEYS", ["contents"])
    errs = v.validate(load_dataset(make_data()), strict=False)
    assert len(errs) == 1 and "contents" in errs[0].message


def test_unknown_desc_language_key_is_error(make_data):
    desc = {**full("x"), "zh_CN": "typo"}
    errs = [i for i in run(make_data(desc=desc), strict=False) if i.level == "error"]
    assert len(errs) == 1 and "zh_CN" in errs[0].message


def test_non_string_desc_value_is_error(make_data):
    desc = {**full("x"), "ja": None}
    errs = [i for i in run(make_data(desc=desc), strict=False) if i.level == "error"]
    assert len(errs) == 1 and "ja" in errs[0].message
