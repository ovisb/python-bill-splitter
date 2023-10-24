# EDU project

## Project

This is _Bill Splitter_ project that is part of Hyperskill platform from Jetbrains Academy.

'Python Core' track

## Technologies and tools used

- Python 3.12
- pytest
- mypy
- isort
- black
- flake8
- make

## Project description

Bill splitter is a simple Python cli application which splits bill evenly between friends. 

It works in the following way:
- asks the user for number of friends
- input each friend name based on above number
- input total bill
- asks if we want to have a lucky person
- if input is lucky, a random winner will be selected and excluded from the split calculation.
- If we don't need a lucky person, bill will be split evenly between all friends.
- final dict with friends names and bill split values will be printed

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

24.10.2023
- Started stage 4
- Moved fetching total bill to common input function
- added better error handling
- Added new 'lucky' functionality where a person who's picked up randomly does not need to pay for the meal, 
hence he's excluded from the bill calculation.
- added stage 4 unit tests
- added github actions CI config
- stage 4 completed

#### Project status
Completed 4/4 stages

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
