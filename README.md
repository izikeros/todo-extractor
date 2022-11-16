<!-- badges -->
[![python versions](https://img.shields.io/pypi/pyversions/todo_extract.svg)](https://pypi.org/project/todo_extract)
[![version](https://img.shields.io/pypi/v/todo_extract.svg)](https://pypi.org/project/todo_extract)
[![codecov](https://codecov.io/gh/izikeros/todo_extract/branch/main/graph/badge.svg)](https://codecov.io/gh/izikeros/todo_extract)
[![dl](https://img.shields.io/pypi/dm/todo_extract)](https://pypi.org/project/todo_extract)
[![Black formatter](https://github.com/izikeros/todo-extractor/actions/workflows/black.yml/badge.svg)](https://github.com/izikeros/todo-extractor/actions/workflows/black.yml)
[![flake8](https://github.com/izikeros/todo-extractor/actions/workflows/flake8.yml/badge.svg)](https://github.com/izikeros/todo-extractor/actions/workflows/flake8.yml)
![License](https://img.shields.io/github/license/izikeros/todo-extractor)
![GitHub contributors](https://img.shields.io/github/contributors/izikeros/todo-extractor)
<!-- end of badges -->

# TODO extractor from text file
Python script for extracting TODO notes from text file.

List can be grouped into sections and can be summarized with stats.


- [Requirements](#requirements)
- [Usage](#usage)
- [Examples](#examples)
  - [extraction of bare list, no stats](#extraction-of-bare-list-no-stats)
  - [extraction of list summarized with stats](#extraction-of-list-summarized-with-stats)
  - [extraction of list divided into sections/chapters](#extraction-of-list-divided-into-sectionschapters)
- [License](#license)


## Installation
```
$ pip install todo-extract
```

## Requirements
The script requires Python3 installed, no other dependencies.

## Usage
```sh
$ todo-extract --help
```

```
usage: todo-extract [-h] [-s] [-c] file_name

Extract todo items from markdown file

positional arguments:
  file_name       markdown file path

optional arguments:
  -h, --help      show this help message and exit
  -s, --stats     display stats
  -c, --chapters  display items grouped by important/not important and done/not done
```

## Examples

### extraction of bare list, no stats
```sh
$ todo-extract file.md
```

output:
```
- buy a bag of chips
- buy a bag of cookies
- buy apples
- buy oranges
- buy bananas
- buy pears
- buy plums
- buy avocados
- buy water
- [!] buy bread
```

### extraction of list summarized with stats
```sh
$ todo-extract --stats file.md
```

```
- buy a bag of chips
- buy a bag of cookies
- buy apples
- buy oranges
- buy bananas
- buy pears
- buy plums
- buy avocados
- buy water
- [!] buy bread

stats:
-------
10  all items (done or not done)
3   not done normal items   (42%  of all normal items are not done)
4   done normal items       (57%  of all normal items are done)
2   important items todo    (66%  of all important items are not done)
1   important items done    (33%  of all important items are done)
```
### extraction of list divided into sections/chapters
```sh
$ todo-extract --chapters file.md
```

```
==== Done normal items: 4 ====

- buy oranges
- buy bananas
- buy pears
- buy plums

==== Important done items: 1 ====

- [!] buy bread

==== Normal todo items: 3 ====

- buy a bag of chips
- buy a bag of cookies
- buy apples

==== Important todo items: 2 ====

- buy avocados
- buy water
```
## License

[MIT](https://izikeros.mit-license.org/) © [Krystian Safjan](https://safjan.com).
