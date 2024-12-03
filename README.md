# datastoragelease
Simple program that checks the size of folders against a .toml file.

## Development
* mypy strict `mypy`
* version control with bumpver `bumpver update --patch --dry`
* isort `uvx isort .`
* ruff `uvx ruff check` `uvx ruff format`

## Build instructions
`pyinstaller --onefile --version-file=VERSION DataStorageLease.py`