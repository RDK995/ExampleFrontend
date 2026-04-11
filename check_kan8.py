#!/usr/bin/env python3

from pathlib import Path


def require(text: str, needle: str, error: str) -> int:
    index = text.find(needle)
    if index == -1:
        raise SystemExit(error)
    return index


def main() -> None:
    source = Path("index.html").read_text(encoding="utf-8")

    header_start = require(source, "React.createElement(\n              'header'", "Missing header section")
    heading_index = require(source, "'Hello React 👋'", "Missing main heading")
    content_section_index = require(
        source,
        "React.createElement(\n              'section',\n              {\n                'aria-labelledby': 'content-heading'",
        "Missing content section",
    )
    content_heading_index = require(source, "'Content'", "Missing content heading")
    sample_copy_index = require(
        source,
        "This sample content section sits directly under the heading area and gives the page a clearer structure.",
        "Missing sample content text",
    )

    if not header_start < heading_index < content_section_index < content_heading_index < sample_copy_index:
        raise SystemExit("Content section is not placed after the header")

    print("KAN-8 check passed")


if __name__ == "__main__":
    main()
