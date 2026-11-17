# Maintaining awesome-geo

Notes for maintainers. Contributors should read [CONTRIBUTING.md](../CONTRIBUTING.md) instead.

## Pre-release checklist

The `awesome-lint` CI job checks repository metadata on GitHub, so it fails until these are done:

- [ ] Set the repository description (Settings, or the "About" box).
- [ ] Add the topics `awesome`, `awesome-list`, `generative-engine-optimization`, `geo`, `ai-search`.
- [ ] Confirm GitHub detects the CC0 license (the repo sidebar should show "CC0-1.0").
- [ ] Enable GitHub Actions, with workflow permissions allowing issues write access (Settings > Actions > General), so link-check issue reporting works.
- [ ] Run `scripts/validate.py --strict` and `scripts/build.py` locally; `git diff` must be empty afterwards.

Set the description and required topics from an authenticated GitHub CLI session:

```bash
gh repo edit --description "A curated list of resources on Generative Engine Optimization (GEO): research, guides, standards, tools and AI search engines." \
  --add-topic awesome --add-topic awesome-list --add-topic generative-engine-optimization --add-topic geo --add-topic ai-search
```

This updates GitHub repository settings and preserves existing topics. After setting them, rerun the failed CI jobs. These settings cannot be supplied by README content or workflow YAML.

`awesome-lint` is pinned in `.github/workflows/ci.yml` (`awesome-lint@2.3.0`). Bump it deliberately and re-check the README.

## Merging a contributor PR

Contributors only supply `desc.en`, but CI on `main` runs `validate.py --strict` and a README sync check. Merging an English-only PR as is turns `main` red. Before merging:

1. Check out the PR branch (`gh pr checkout <number>`).
2. List missing translations: `.venv/bin/python scripts/missing.py --format yaml`.
3. Fill them in, following `docs/translation/<lang>.md` and `docs/translation/product-names.md`.
4. Run `.venv/bin/python scripts/validate.py --strict` and `.venv/bin/python scripts/build.py`.
5. Commit the data and regenerated `README*.md` to the PR branch and push.
6. Merge.

## 维护者说明（中文）

发布前请在 GitHub 上完成：设置仓库描述；添加主题 `awesome`、`awesome-list`、`generative-engine-optimization`、`geo`、`ai-search`；确认 GitHub 识别出 CC0 许可证；启用 Actions，并授予 issues 写权限。

合并贡献者 PR 前：检出 PR 分支，运行 `scripts/missing.py --format yaml`，按 `docs/translation/<lang>.md` 与 `product-names.md` 补全翻译，运行 `scripts/validate.py --strict` 与 `scripts/build.py`，把改动提交到 PR 分支，然后再合并。否则仅含英文的条目会使 `main` 上的严格校验与 README 同步检查失败。
