# EDU project

## Project

This is _Bill Splitter_ project that is part of Hyperskill platform from Jetbrains Academy.

'Python Core' track

## Technologies and tools used

- Python 3.11
- pytest
- mypy
- isort
- black
- flake8
- make

## Project description

To add...

## Changelog

24.10.2023
- Initial github repo creation + project structure
- Taking input from user about the amount of friends he wants to invite
- Based on the amount of friends, take input for friend names and store them in a dictionary
- Added stage 1 unit tests
- Stage 1 completed

24.10.2023
- Started stage 2
- Added function for splitting total bill evenly 
- added stage 2unit tests
- stage 2 completed

24.10.2023
- Started stage 3
- Added function for randomly choosing name from the friends dict
- added stage 3 unit tests
- stage 3 completed

#### Project status
Completed 3/4 stages

#### Install steps

Install everything (main + dev packages except optional groups)

```sh
peotry install
```

Install main packages only

```sh
peotry install --only main

```

If you need pre-commit

```sh
poetry install --with commit
```

If you decided to install pre-commit you can install .pre-commit files in your repo

```sh
peotry run pre-commit install -t pre-commit
poetry run pre-commit install -t pre-push
```

If the files are git staged, you can trigger pre-commit manually

```sh
poetry run pre-commit run --all-files
poetry run pre-commit run --hook-stage push -v
```

#### Makefile

Added 'Makefile' to make it easy to validate files
Check bellow command on usage

```sh
make help
```
