#!/usr/bin/env python3

# program that takes a markdown file as cli input argument and extracts the "todo items"
# and prints them to stdout.
# items are marked with a '- [ ]'
# items scan be marked as done with '- [x]'
# items can be marked as important with '- [!]'
# items can be marked as done and important with '- [x] [!]'
# items can be preceded with whitespaces and newlines
import argparse
import getopt
import sys
import re


def is_important(item):
    important = False
    if item.strip().startswith("[!]"):
        important = True

    if item.replace(" ", "").replace("[", "").replace("]", "").startswith("!"):
        important = True
    return important


def main(filename, stats):

    # read markdown file
    with open(filename, "rt") as f:
        markdown = f.read()
    # extract todo items in one of formats: '- [ ]', '- [x]', '- [!]', '- [x] [!]'
    # todo_items = re.findall(r'^\s*-\s*\[\s*(x|\!|\]\s*)\s*\]\s*', markdown, re.MULTILINE)
    todo_items = re.findall(
        r"^\s*-\s*\[\s*(x|\!|)\s*\]\s*(.*)$", markdown, re.MULTILINE
    )
    todo_items = [(" ", item[1]) if item[0] == "" else item for item in todo_items]

    n_all = len(todo_items)
    done_items = [item for item in todo_items if item[0] == "x"]
    n_done = len(done_items)
    important_items = [item for item in todo_items if item[0] == "!"]
    n_important = len(important_items)
    important_done = [item for item in done_items if is_important(item[1])]
    n_done_important = len(important_done)

    # print items
    # TODO: KS: 2022-03-11: add option to print items in groups important/not important
    for item in todo_items:
        print(f"[{item[0]}] {item[1]}")

    if stats:
        print("\nstats:\n-------")
        # print number of items
        print(f"{str(n_all):3s} {'100%':4s} todo items")

        try:
            # print number of done items
            print(f"{str(n_done):3s} {str(int(100*n_done/n_all))+'%':4s} done items")
        except ZeroDivisionError:
            print("0 0% done items")

        # print number of important items
        try:
            print(
                f"{str(n_important):3s} {str(int(100*n_important/n_all))+'%':4s} important items"
            )
        except ZeroDivisionError:
            print("{'0':3s} {'0%':4s} important items")

        try:
            # print number of done and important items
            print(
                f"{str(n_done_important):3s} {str(int(100*n_done_important/n_important))+'%':4s} important items done"
            )
        except ZeroDivisionError:
            print(f"{'0':3s} {'0%':4s} important items done")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract todo items from markdown file"
    )
    # positional arguments
    parser.add_argument("file_name", help="markdown file path")

    # named parameters
    parser.add_argument(
        "-s",
        "--stats",
        action="store_true",
        help="display stats",
        default=False,
    )

    args = parser.parse_args()
    main(args.file_name, args.stats)
