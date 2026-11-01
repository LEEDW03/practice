"""Convert files to Markdown with Microsoft MarkItDown.

Usage:
    python convert.py FILE [FILE ...] [-o OUTPUT_DIR]

Each input is converted and written to OUTPUT_DIR/<filename>.md (e.g. report.pdf.md)
(default: ./output). Supported inputs include PDF, DOCX, PPTX,
XLSX, HTML, CSV, JSON, XML, images, and more.
"""

import argparse
import sys
from pathlib import Path

from markitdown import MarkItDown


def convert(paths: list[Path], out_dir: Path) -> int:
    md = MarkItDown()
    out_dir.mkdir(parents=True, exist_ok=True)
    failures = 0
    for path in paths:
        try:
            result = md.convert(str(path))
        except Exception as exc:  # report and keep going
            print(f"FAIL {path}: {exc}", file=sys.stderr)
            failures += 1
            continue
        target = out_dir / f"{path.name}.md"
        target.write_text(result.text_content, encoding="utf-8")
        print(f"OK   {path} -> {target}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("-o", "--output", type=Path, default=Path("output"))
    args = parser.parse_args()
    return 1 if convert(args.files, args.output) else 0


if __name__ == "__main__":
    sys.exit(main())
