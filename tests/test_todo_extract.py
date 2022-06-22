from unittest import TestCase

from todo_extract import markdown_extractor


class Test(TestCase):
    def test_markdown_extractor__bare(self):
        markdown_extractor(filename="text_with_todos.md", stats=False, sections=False)

    def test_markdown_extractor__with_stats(self):
        markdown_extractor(filename="text_with_todos.md", stats=True, sections=False)

    def test_markdown_extractor__with_sections(self):
        markdown_extractor(filename="text_with_todos.md", stats=False, sections=True)

    def test_markdown_extractor__with_stats_and_sections(self):
        markdown_extractor(filename="text_with_todos.md", stats=True, sections=True)
