# practice — MarkItDown

Convert documents to Markdown with [Microsoft MarkItDown](https://github.com/microsoft/markitdown).

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python convert.py samples/sample.html samples/sample.csv
# OK   samples/sample.html -> output/sample.html.md
```

Use `-o DIR` to choose the output folder (default `output/`).

You can also use the CLI that ships with MarkItDown:

```bash
markitdown path/to/file.pdf -o file.md
```

Supported inputs: PDF, Word, PowerPoint, Excel, HTML, CSV, JSON, XML, ZIP, images (EXIF/OCR with an LLM), audio (transcription), EPub, and more.
