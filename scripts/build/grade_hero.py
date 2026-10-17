"""Colour-grade the homepage hero photo into a warm, cinematic dusk look (EXIF dropped on save).

Usage: python scripts/build/grade_hero.py <full-size source photo>
Writes assets/hero/dhaka-cinematic-{2400,1200}.webp (16:9) and dhaka-cinematic-portrait.webp (2:3).
"""
import os, sys
import numpy as np
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "assets", "hero")


def smooth(a, b, x):
    t = np.clip((x - a) / (b - a), 0, 1)
    return t * t * (3 - 2 * t)


def grade(im):
    a = np.asarray(im, dtype=np.float32) / 255
    h = a.shape[0]
    lum = a @ np.array([.3, .59, .11], dtype=np.float32)
    desat = lum[..., None] + (a - lum[..., None]) * .8
    # warm gradient map: deep brown shadows, amber mids, cream highlights
    stops = np.array([[0, .07, .045, .03], [.45, .5, .32, .21], [.75, .86, .62, .42], [1, 1, .9, .74]], dtype=np.float32)
    mapped = np.stack([np.interp(lum, stops[:, 0], stops[:, i]) for i in (1, 2, 3)], -1)
    out = mapped * .4 + desat * .6
    # sunset sky: bright pixels near the top turn orange
    y = np.linspace(0, 1, h, dtype=np.float32)[:, None]
    w = (np.clip(1 - y / .58, 0, 1) ** 1.2) * smooth(.42, .8, lum)
    # sky colour runs from deep orange at the top to a dusty rose haze at the horizon
    t = np.clip(y / .5, 0, 1)[..., None]
    sky = np.array([.86, .45, .17], dtype=np.float32) * (1 - t) + np.array([.78, .58, .5], dtype=np.float32) * t
    out = out * (1 - .8 * w[..., None]) + sky * (.4 + .6 * lum[..., None]) * .8 * w[..., None] / .75
    out = np.clip(.5 + (out - .5) * 1.1, 0, 1) * .9
    return Image.fromarray((out * 255).astype(np.uint8))


def crop(im, ratio, fx=.5, fy=.5):
    w, h = im.size
    if w / h > ratio:
        nw = round(h * ratio); x = round((w - nw) * fx); return im.crop((x, 0, x + nw, h))
    nh = round(w / ratio); y = round((h - nh) * fy); return im.crop((0, y, w, y + nh))


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    src = grade(ImageOps.exif_transpose(Image.open(sys.argv[1])).convert("RGB"))
    wide = crop(src, 16 / 9, fy=.3)
    for width in (2400, 1200):
        wide.resize((width, round(width * 9 / 16)), Image.LANCZOS).save(os.path.join(OUT, f"dhaka-cinematic-{width}.webp"), quality=82, method=6)
    crop(src, 2 / 3, fx=.5).resize((1080, 1620), Image.LANCZOS).save(os.path.join(OUT, "dhaka-cinematic-portrait.webp"), quality=80, method=6)
    print("wrote", sorted(os.listdir(OUT)))
