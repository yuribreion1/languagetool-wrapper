# LanguageTool Wrapper

The repository offers basic wrappers for [LanguageTool](https://languagetool.org) which is the
AI/ML platform that helps with language grammar mistakes.

# How to use it?

1. Consider creating the conda environment:
- `conda env create -f environment.yml`
2. Prepare the following environment variables for authentication:
  - `LANGUAGETOOL_USERNAME`
  - `LANGUAGETOOL_APIKEY`
  - `LANGUAGETOOL_BASEURL`
3. Use the python command line to run the `main.py` with the
following arguments:
- Required: `--function languages|check`
- Required if `check` is selected: `--language` and `--text` (plain-text or JSON)

Example of `language`: **pt-BR**

# Files Overview

## `api_client.py`

File that hosts the APIClient class, that is responsible to handle the HTTP requests.
`requests`library is that takes the action to interact with external applications.

### Contructor

The class has a constructor that expects three arguments:
- `base_url`
- `username`
- `apikey`

### `get`

The function obtain languages available by language tool, and obtain the words stored
on the user dictionary.

### `post`

Action to send information to language tool, specially to verify markup or plain texts.
Additionally, the `post` action also add new words to the user dictionary.
