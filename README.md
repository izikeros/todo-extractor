# TODO extractor from markdown file
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
MIT
