# LanguageTool Wrapper

The repository offers basic wrappers for [LanguageTool](https://languagetool.org) which is the
AI/ML platform that helps with language grammar mistakes.

# How to use it?

1. Consider creating the conda environment:
- `conda env create -f environment.yml`
2. Use the python command line to run the `main.py` with the
following arguments:
- Required: `--function languages|check`
- Required if `check` is selected: `--language` and `--text` (plain-text or JSON)

Example of `language`: **pt-BR**
