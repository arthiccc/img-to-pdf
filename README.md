```md
# WhatsApp Screenshot → Print-ready PDF

A tiny Python script that takes a folder of images (WhatsApp screenshots, receipts, etc.) and generates a single PDF laid out in a grid (e.g., **4 images per page**) without stretching (aspect ratio preserved). It also fixes common “sideways” phone screenshots using EXIF orientation. :contentReference[oaicite:0]{index=0}

## Features
- Batch images → one PDF
- Layout: `--per-page` (commonly `4` for 2×2)
- No distortion (keeps aspect ratio)
- EXIF orientation fix (`ImageOps.exif_transpose`) :contentReference[oaicite:1]{index=1}
- Uses ReportLab canvas (`showPage()` / `save()`) :contentReference[oaicite:2]{index=2}

## Requirements
- Python 3.x
- Packages: `pillow`, `reportlab`

## Install
Using **uv** (recommended):
```powershell
uv pip install pillow reportlab
```

`uv run` ensures you execute inside the same environment you installed into. [Astral Docs+1](https://docs.astral.sh/uv/guides/scripts/?utm_source=chatgpt.com)

Or with pip:

```powershell
pip install pillow reportlab
```

## Usage

Generate a PDF with **4 images per page** (A4):

```powershell
uv run python make_print_pdf.py "C:\path\to\images" output.pdf --per-page 4 --pagesize A4
```

Common options:

-   `--per-page` : 1 / 2 / 4 / 6 / 8 (depends on script version)
    
-   `--pagesize` : `A4` or `LETTER`
    
-   `--margin-mm` : adjust whitespace
    
-   `--auto-rotate` : rotate 90° only if it fills the cell better (still no stretching)
    

See all options:

```powershell
uv run python make_print_pdf.py --help
```

## Notes

-   Put all screenshots/images into one folder first (unzip if needed), then run the command above.
    
-   If images look too big/small: tweak `--margin-mm` (bigger margin = smaller images).
    

## License

MIT (or pick your preferred license)

```makefile
::contentReference[oaicite:4]{index=4}
```

You: 

too longgg

ChatGPT: 

Thought for 13s

```md
# WhatsApp Screenshots → Print PDF

Convert a folder of images (e.g., WhatsApp screenshots) into **one printable PDF** in a grid (e.g., **4 per page**). Keeps aspect ratio (no stretching) and fixes common sideways phone screenshots (EXIF orientation).

## Install
```powershell
uv pip install pillow reportlab
```

## Run (4 per page)

```powershell
uv run python make_print_pdf.py "C:\path\to\images" output.pdf --per-page 4 --pagesize A4
```

## Useful options

-   `--per-page` : 1 / 2 / 4 / 6 / 8 (depending on script)
    
-   `--pagesize` : `A4` or `LETTER`
    
-   `--margin-mm` : whitespace around the page
    
-   `--auto-rotate` : rotate 90° only if it fills the cell better (still no stretching)
    

```powershell
uv run python make_print_pdf.py --help
```

```perl
Sources (why these commands/features work):
- `uv run` runs scripts in the project environment so your installed deps resolve correctly. :contentReference[oaicite:0]{index=0}  
- `ImageOps.exif_transpose()` applies EXIF Orientation correctly (and returns a new image). :contentReference[oaicite:1]{index=1}  
- ReportLab uses `canvas.showPage()` per page and `canvas.save()` to write the PDF. :contentReference[oaicite:2]{index=2}
::contentReference[oaicite:3]{index=3}
```
