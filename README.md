# resume

[![tests](https://github.com/ianlewis/resume/actions/workflows/pre-submit.units.yml/badge.svg)](https://github.com/ianlewis/resume/actions/workflows/pre-submit.units.yml) [![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/ianlewis/resume/badge)](https://securityscorecards.dev/viewer/?uri=github.com%2Fianlewis%2Fresume)

My resume is written in LaTeX using
[`resume.cls`](./third_party/csuros@cs.yale.edu/resume.cls) by [Miklós
Csűrös](https://diro.umontreal.ca/repertoire-departement/professeurs/professeur/in/in14308/sg/Mikl%C3%B3s%20Cs%C5%B1r%C3%B6s/).

## Requirements

- `pdflatex`: For generating the PDF.
- `chktex`: For linting Latex files.

## Build resume PDF

```shell
make Ian_M_Lewis_Resume.pdf
```
