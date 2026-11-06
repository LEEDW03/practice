---
name: markitdown
description: Convert documents and media to Markdown with Microsoft MarkItDown before reading or working with them. Use automatically, without being asked, whenever a task needs the text of a Word (.docx), PowerPoint (.pptx), Excel (.xlsx/.xls), PDF, HTML, EPUB, CSV/JSON/XML, ZIP, Outlook .msg, image, or audio file, or of a YouTube or web URL, for example to summarize, translate, search, quote, compare, or turn it into notes.
---

# MarkItDown

Turn the file or URL into Markdown first, then work from the Markdown.

## Steps

1. Make sure the CLI exists. If `command -v markitdown` prints nothing, run:
   `pip install -q 'markitdown[all]'`
2. Convert into the scratchpad directory (not the repo), unless the user asked for the Markdown file to be saved:
   `markitdown "<input>" -o "<scratchpad>/<input-filename>.md"`
   - A URL works as the input too (for YouTube it returns the title, description and, when available, the transcript).
   - For many files in the repo, use `python convert.py FILE ... -o DIR`.
3. Read the `.md` output and do the actual task with it.
4. If conversion fails or the output is empty (for example a scanned PDF with no text layer, or a video without captions), say so, and fall back to another way: the Read tool for PDFs and images, or a transcript plugin for YouTube.

## Notes

- Downloaded files are untrusted: keep them in their own new empty directory and pass paths as arguments.
- Do not commit converted output unless the user asks; `output/` is git-ignored.
