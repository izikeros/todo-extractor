#!/usr/bin/env python3
"""
Program extracts the "todo items" from the text file and prints them to stdout.

Convention for items:
items are marked with a '- [ ]'
items scan be marked as done with '- [x]'
items can be marked as important with '- [!]'
items can be marked as done and important with '- [x] [!]'
items can be preceded with whitespaces and newlines
"""

import re
from pathlib import Path
from typing import Dict
from typing import List
from typing import NoReturn
from typing import Union


def is_important(item: str) -> bool:
    important = False
    if item.strip().startswith("[!]"):
        important = True

    if item.replace(" ", "").replace("[", "").replace("]", "").startswith("!"):
        important = True
    return important


def markdown_extractor(
    filename: Union[str, Path], stats: bool, sections: bool
) -> NoReturn:
    # read markdown file
    markdown = Path(filename).read_text()
    # extract todo items in one of formats: '- [ ]', '- [x]', '- [!]', '- [x] [!]'
    # todo_items = re.findall(r'^\s*-\s*\[\s*(x|\!|\]\s*)\s*\]\s*', markdown, re.MULTILINE)
    todo_items = re.findall(
        pattern=r"^\s*-\s*\[\s*(x|\!|)\s*\]\s*(.*)$",
        string=markdown,
        flags=re.MULTILINE,
    )
    todo_items = [(" ", item[1]) if item[0] == "" else item for item in todo_items]

    # print items
    items = categorize_items(todo_items=todo_items)
    counts = calculate_stats(todo_items=todo_items, items=items)
    handle_sections(sections=sections, todo_items=todo_items, items=items, c=counts)
    handle_stats(c=counts, stats=stats)


def categorize_items(todo_items: List[str]) -> Dict[str, List[str]]:
    done_items = [item for item in todo_items if item[0] == "x"]
    return {
        "done_items": done_items,
        "normal_done_items": [item for item in done_items if not is_important(item[1])],
        "important_todo": [item for item in todo_items if item[0] == "!"],
        "important_done": [item for item in done_items if is_important(item[1])],
        "normal_todo": [item for item in todo_items if item[0] == " "],
    }


def calculate_stats(
    todo_items: List[str], items: Dict[str, List[str]]
) -> Dict[str, int]:
    n_all = len(todo_items)
    n_done_normal = len(items["normal_done_items"])
    # important not done

    n_important_todo = len(items["important_todo"])
    # important not done

    n_done_important = len(items["important_done"])

    n_normal_todo = len(items["normal_todo"])

    counts = {
        "n_all": n_all,
        "n_done_important": n_done_important,
        "n_done_normal": n_done_normal,
        "n_important_todo": n_important_todo,
        "n_normal_todo": n_normal_todo,
    }
    return counts


def handle_stats(c: Dict[str, int], stats: bool) -> NoReturn:
    if not stats:
        return

    print("\nstats:\n-------")
    # print number of items
    print(f"{str(c['n_all']):3s} all items (done or not done)")

    try:
        # print number of not done normal items
        ndn = "not done normal items"
        ndn_pct = int(
            100 * c["n_normal_todo"] / (c["n_done_normal"] + c["n_normal_todo"])
        )
        print(
            f"{str(c['n_normal_todo']):3s} {ndn:23s} ({f'{ndn_pct}%':4s} of all normal"
            " items are not done)"
        )

    except ZeroDivisionError:
        print("0 0% done items")

    try:
        # print number of done normal items
        dn = "done normal items"
        dn_pct = int(
            100 * c["n_done_normal"] / (c["n_done_normal"] + c["n_normal_todo"])
        )
        print(
            f"{str(c['n_done_normal']):3s} {dn:23s} ({f'{dn_pct}%':4s} of all normal"
            " items are done)"
        )

    except ZeroDivisionError:
        print("0 0% done items")

        # print number of important items
    try:
        ind = "important items todo"
        ind_pct = int(
            100
            * c["n_important_todo"]
            / (c["n_important_todo"] + c["n_done_important"])
        )
        print(
            f"{str(c['n_important_todo']):3s} {ind:23s} ({f'{ind_pct}%':4s} of all"
            " important items are not done)"
        )

    except ZeroDivisionError:
        print("{'0':3s} {'0%':4s} important items")

    try:
        # print number of done and important items
        iid = "important items done"
        iid_pct = int(
            100
            * c["n_done_important"]
            / (c["n_important_todo"] + c["n_done_important"])
        )
        print(
            f"{str(c['n_done_important']):3s} {iid:23s} ({f'{iid_pct}%':4s} of all"
            " important items are done)"
        )

    except ZeroDivisionError:
        print(f"{'0':3s} {'0%':4s} important items done")


def handle_sections(
    sections: bool,
    todo_items: List[str],
    items: Dict[str, List[str]],
    c: Dict[str, int],
) -> NoReturn:
    if sections:
        # done items
        print(f"\n==== Done normal items: {c['n_done_normal']} ====\n")
        for item in items["normal_done_items"]:
            print(f"- {item[1]}")

        # important done items
        print(f"\n==== Important done items: {c['n_done_important']} ====\n")
        for item in items["important_done"]:
            print(f"- {item[1]}")

        # Normal todo items
        print(f"\n==== Normal todo items: {c['n_normal_todo']} ====\n")
        for item in items["normal_todo"]:
            print(f"- {item[1]}")

        # important items
        print(f"\n==== Important todo items: {c['n_important_todo']} ====\n")
        for item in items["important_todo"]:
            print(f"- {item[1]}")

    else:
        for item in todo_items:
            print(f"- {item[1]}")
