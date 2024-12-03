# datastoragelease
Simple program that checks the size of folders against a .toml file.

## Development
* mypy strict `mypy`
* version control with bumpver `bumpver update --patch --dry`
* isort `uvx isort .`
* ruff `uvx ruff check` `uvx ruff format`

## Build instructions
`pyinstaller --onefile --version-file=VERSION DataStorageLease.py`

## Example DataStorageLease.toml
```
PC = "AC0130"

[JDoe]
amount = "1TB"
untill = 2025-01-01
# image analysis project

[Presley]
amount = "500GB"
untill = 2024-12-01
# needs it for music project

[Sagan]
amount = "500GB"
untill = 2100-01-01
# permanent storage
```
