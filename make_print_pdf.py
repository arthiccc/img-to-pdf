# make_print_pdf.py
# deps: pillow, reportlab
# Example:
#   uv run python make_print_pdf.py "C:\path\to\images" output.pdf --per-page 8 --pagesize A4 --auto-rotate --margin-mm 10 --shrink 0.95

import os
import sys
import argparse
from PIL import Image, ImageOps
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.utils import ImageReader

IMG_EXTS = (".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff")


def list_images(folder: str):
    files = []
    for name in os.listdir(folder):
        if name.lower().endswith(IMG_EXTS):
            files.append(os.path.join(folder, name))
    return sorted(files, key=lambda p: os.path.basename(p).lower())


def fit_into_box(img_w: float, img_h: float, box_w: float, box_h: float):
    """Scale to fit within box while preserving aspect ratio (no stretching)."""
    scale = min(box_w / img_w, box_h / img_h)
    return img_w * scale, img_h * scale


def best_fit_image(im: Image.Image, box_w: float, box_h: float, allow_rotate: bool):
    """
    Fix EXIF orientation; optionally rotate 90° only if it fills the cell better.
    (Still no stretching.)
    """
    im = ImageOps.exif_transpose(im)  # must assign return value :contentReference[oaicite:2]{index=2}

    w, h = im.size
    dw1, dh1 = fit_into_box(w, h, box_w, box_h)
    best_im, best_dw, best_dh, best_area = im, dw1, dh1, dw1 * dh1

    if allow_rotate:
        dw2, dh2 = fit_into_box(h, w, box_w, box_h)
        if (dw2 * dh2) > best_area:
            best_im = im.rotate(90, expand=True)
            best_dw, best_dh = dw2, dh2

    return best_im, best_dw, best_dh


def grid_for(per_page: int):
    # Layouts tuned for A4 portrait printing
    if per_page == 1:
        return 1, 1
    if per_page == 2:
        return 2, 1
    if per_page == 4:
        return 2, 2
    if per_page == 6:
        return 3, 2
    if per_page == 8:
        return 4, 2
    raise ValueError("Unsupported --per-page. Use 1, 2, 4, 6, or 8.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder", help="Folder containing images")
    ap.add_argument("output", help="Output PDF path, e.g. output.pdf")
    ap.add_argument("--per-page", type=int, default=8, choices=[1, 2, 4, 6, 8], help="Images per page")
    ap.add_argument("--pagesize", default="A4", choices=["A4", "LETTER"], help="Page size")
    ap.add_argument("--margin-mm", type=float, default=10.0, help="Page margin in mm")
    ap.add_argument(
        "--auto-rotate",
        action="store_true",
        help="Rotate 90° only if it fills the cell better (no stretching).",
    )
    ap.add_argument(
        "--shrink",
        type=float,
        default=1.0,
        help="Extra shrink inside each cell (e.g. 0.9 makes everything 10%% smaller).",
    )
    args = ap.parse_args()

    imgs = list_images(args.folder)
    if not imgs:
        print("No images found in folder:", args.folder)
        sys.exit(1)

    page_w, page_h = A4 if args.pagesize == "A4" else letter
    margin = args.margin_mm * 72.0 / 25.4  # mm -> points (1pt = 1/72 inch) :contentReference[oaicite:3]{index=3}

    rows, cols = grid_for(args.per_page)
    cell_w = (page_w - 2 * margin) / cols
    cell_h = (page_h - 2 * margin) / rows

    shrink = max(0.1, min(float(args.shrink), 1.0))

    c = canvas.Canvas(args.output, pagesize=(page_w, page_h))

    i = 0
    while i < len(imgs):
        for r in range(rows):
            for col in range(cols):
                if i >= len(imgs):
                    break

                path = imgs[i]
                i += 1

                try:
                    im = Image.open(path).convert("RGB")
                except Exception as e:
                    print(f"Skipping unreadable image: {path}\n  Error: {e}")
                    continue

                im, draw_w, draw_h = best_fit_image(im, cell_w, cell_h, allow_rotate=args.auto_rotate)
                draw_w *= shrink
                draw_h *= shrink

                x = margin + col * cell_w + (cell_w - draw_w) / 2
                y = page_h - margin - (r + 1) * cell_h + (cell_h - draw_h) / 2

                # drawImage is the preferred image method in ReportLab's canvas :contentReference[oaicite:4]{index=4}
                c.drawImage(ImageReader(im), x, y, width=draw_w, height=draw_h, mask="auto")

        c.showPage()

    c.save()
    print("Saved:", args.output)


if __name__ == "__main__":
    main()
