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
