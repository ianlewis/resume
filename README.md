# resume

[![tests](https://github.com/ianlewis/resume/actions/workflows/pull_request.tests.yml/badge.svg)](https://github.com/ianlewis/resume/actions/workflows/pull_request.tests.yml)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/ianlewis/resume/badge)](https://securityscorecards.dev/viewer/?uri=github.com%2Fianlewis%2Fresume)

My resume is written in LaTeX.

## Requirements

- `lualatex`: For generating the PDF.
- `chktex`: For linting Latex files.

You can install these dependencies on Debian/Ubuntu with the following commands:

```bash
TEXLIVE_BASE_VERSION="2023.20240207-1"
TEXLIVE_EXTRA_VERSION="${TEXLIVE_BASE_VERSION}"
TEXLIVE_LANG_VERSION="${TEXLIVE_BASE_VERSION}"
sudo apt-get update
sudo apt-get install -y chktex
sudo apt-get install -y \
    --no-install-recommends \
    texlive-latex-base="${TEXLIVE_BASE_VERSION}" \
    texlive-luatex="${TEXLIVE_BASE_VERSION}" \
    texlive-latex-extra="${TEXLIVE_EXTRA_VERSION}" \
    texlive-lang-japanese"${TEXLIVE_LANG_VERSION}"
```

## Build resume PDF

```shell
make Ian_M_Lewis_Resume.pdf
make Ian_M_Lewis_Resume.ja.pdf
```
