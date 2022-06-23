import os
from pathlib import Path
from unittest import TestCase

from todo_extract import markdown_extractor


def get_project_root() -> Path:
    return Path(os.path.dirname(os.path.realpath(__file__))).parent


file_name = get_project_root() / "tests" / "text_with_todos.md"


class Test(TestCase):
    # TODO: KS: 2022-06-23: Parametrize this test
    def test_markdown_extractor__bare(self):
        markdown_extractor(filename=file_name, stats=False, sections=False)

    def test_markdown_extractor__with_stats(self):
        markdown_extractor(filename=file_name, stats=True, sections=False)

    def test_markdown_extractor__with_sections(self):
        markdown_extractor(filename=file_name, stats=False, sections=True)

    def test_markdown_extractor__with_stats_and_sections(self):
        markdown_extractor(filename=file_name, stats=True, sections=True)
