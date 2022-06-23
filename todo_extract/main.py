import argparse

from . import version
from .todo_extract import markdown_extractor


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract todo items from markdown file"
    )

    parser.add_argument("file_name", help="markdown file path")

    parser.add_argument(
        "-s",
        "--stats",
        action="store_true",
        help="display stats",
        default=False,
    )

    parser.add_argument(
        "-c",
        "--chapters",
        action="store_true",
        help="display items grouped by important/not important and done/not done",
        default=False,
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {version.__version__}"
    )

    args = parser.parse_args()
    markdown_extractor(
        filename=args.file_name, stats=args.stats, sections=args.chapters
    )
