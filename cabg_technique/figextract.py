#!/usr/bin/env python3
"""Extract embedded raster artwork at native resolution.

The skill's extract_images.py composites onto a white background via
fitz.Pixmap(pix.colorspace, ...), which throws when the embedded image has no
colorspace (image masks / some CMYK JPEGs — e.g. the 1200-dpi line art in the
Ricci ATS paper). Pulling the raw stream with doc.extract_image() avoids that
and keeps the artwork unresampled.

usage: figextract.py <pdf> <page> <xref> <out.png> [<page> <xref> <out.png> ...]
"""
import io, sys
import fitz
from PIL import Image


def grab(doc, xref, out):
    info = doc.extract_image(xref)
    im = Image.open(io.BytesIO(info["image"]))
    if im.mode in ("CMYK", "P", "LA", "RGBA"):
        if im.mode in ("LA", "RGBA"):
            bg = Image.new("RGB", im.size, (255, 255, 255))
            bg.paste(im, mask=im.split()[-1])
            im = bg
        else:
            im = im.convert("RGB")
    elif im.mode == "1":
        im = im.convert("L")
    im.save(out)
    return f"{out}  {im.size[0]}x{im.size[1]}  {im.mode}"


if __name__ == "__main__":
    pdf, rest = sys.argv[1], sys.argv[2:]
    doc = fitz.open(pdf)
    for i in range(0, len(rest), 3):
        _page, xref, out = rest[i], int(rest[i + 1]), rest[i + 2]
        print(grab(doc, xref, out))
    doc.close()
