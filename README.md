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
