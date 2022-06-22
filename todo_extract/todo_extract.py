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


def is_important(item):
    important = False
    if item.strip().startswith("[!]"):
        important = True

    if item.replace(" ", "").replace("[", "").replace("]", "").startswith("!"):
        important = True
    return important


def markdown_extractor(filename, stats, sections):

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
    normal_done_items = [item for item in done_items if not is_important(item[1])]
    n_done_normal = len(normal_done_items)

    # important not done
    important_todo = [item for item in todo_items if item[0] == "!"]
    n_important_todo = len(important_todo)

    # important not done
    important_done = [item for item in done_items if is_important(item[1])]
    n_done_important = len(important_done)

    normal_todo = [item for item in todo_items if item[0] == " "]
    n_normal_todo = len(normal_todo)

    # print items
    # TODO: KS: 2022-03-11: add option to print items in groups important/not important
    if sections:
        # done items
        print("\n==== Done normal items: {} ====\n".format(n_done_normal))
        for item in normal_done_items:
            print(f"- {item[1]}")

        # important done items
        print("\n==== Important done items: {} ====\n".format(n_done_important))
        for item in important_done:
            print(f"- {item[1]}")

        # Normal todo items
        print("\n==== Normal todo items: {} ====\n".format(n_normal_todo))
        for item in normal_todo:
            print(f"- {item[1]}")

        # important items
        print("\n==== Important todo items: {} ====\n".format(n_important_todo))
        for item in important_todo:
            print(f"- {item[1]}")

    else:
        for item in todo_items:
            print(f"- {item[1]}")

    if stats:
        print("\nstats:\n-------")
        # print number of items
        print(
            f"{str(n_all):3s} all items (done or not done)"
        )

        try:
            # print number of not done normal items
            ndn = 'not done normal items'
            ndn_pct = int(100 * n_normal_todo / (n_done_normal + n_normal_todo))
            print(
                f"{str(n_normal_todo):3s} {ndn:23s} ({str(ndn_pct) + '%':4s} of all normal items are not done)"
            )
        except ZeroDivisionError:
            print("0 0% done items")

        try:
            # print number of done normal items
            dn = 'done normal items'
            dn_pct = int(100 * n_done_normal / (n_done_normal + n_normal_todo))
            print(
                f"{str(n_done_normal):3s} {dn:23s} ({str(dn_pct) + '%':4s} of all normal items are done)"
            )
        except ZeroDivisionError:
            print("0 0% done items")

        # print number of important items
        try:
            ind = 'important items todo'
            ind_pct = int(100 * n_important_todo / (n_important_todo + n_done_important))
            print(
                f"{str(n_important_todo):3s} {ind:23s} ({str(ind_pct) + '%':4s} of all important items are not done)"
            )
        except ZeroDivisionError:
            print("{'0':3s} {'0%':4s} important items")

        try:
            # print number of done and important items
            iid = 'important items done'
            iid_pct = int(100 * n_done_important / (n_important_todo + n_done_important))
            print(
                f"{str(n_done_important):3s} {iid:23s} ({str(iid_pct) + '%':4s} of all important items are done)"
            )
        except ZeroDivisionError:
            print(f"{'0':3s} {'0%':4s} important items done")
