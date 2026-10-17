"""Crop brand photos to 9:16 for the Instagram promo (EXIF dropped on save)."""
import os, sys
from PIL import Image, ImageFilter, ImageOps, ImageStat
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRIVE = sys.argv[1] if len(sys.argv) > 1 else ""
OUT = os.path.join(ROOT, "promo", "img")
W, H = 1296, 2304  # 1.2x the 1080x1920 frame, room for zoom
# name -> horizontal focus (0 = left edge, 1 = right edge)
PICKS = {
    "traffic-approach-led-tower": .5, "gulshan-led-skyline": .5, "busy-junction-billboard": .5,
    "roadside-led-flyover-junction": .5, "expressway-billboard-close": .78,
    "expressway-static-billboards": .32, "gulshan-circle-led-cluster": .5, "night-street-led-dhaka": .5,
    "multi-format-building-advertising": .5, "tower-top-led-screen": .5, "airport-terminal-led-arrivals": .5,
    "concert-stage-crowd": .5, "opening-day-crowd": .5, "large-format-printing": .5, "police-plaza-led-night": .5,
    "outdoor/metro-train-interior": .5,
}
# Third-party "call for ad" phone numbers painted out, as (left, top, right, bottom) fractions of the source photo
REDACT = {"expressway-static-billboards": [(.385, .362, .445, .398)]}
FOCUS = dict(PICKS)
FOCUS.update({k: float(v) for k, v in (a.split("=") for a in sys.argv[2:])})

def source(name):
    if name.startswith("outdoor/"):
        return os.path.join(ROOT, "assets", name + ".webp")
    full = os.path.join(DRIVE, "full", name + ".jpg") if DRIVE else ""
    return full if full and os.path.exists(full) else os.path.join(ROOT, "assets", "field", name + "-1600.webp")

os.makedirs(OUT, exist_ok=True)
for name, fx in FOCUS.items():
    im = ImageOps.exif_transpose(Image.open(source(name))).convert("RGB")
    for fl, ft, fr, fb in REDACT.get(name, []):
        box = tuple(round(v) for v in (fl * im.width, ft * im.height, fr * im.width, fb * im.height))
        pad = round(im.width * .01)
        ring = im.crop((box[0], box[3], box[2], box[3] + 2 * pad))  # the board just below the sign
        im.paste(tuple(round(c) for c in ImageStat.Stat(ring).median), box)
        soft = (box[0] - pad, box[1], box[2] + pad, box[3] + pad)
        im.paste(im.crop(soft).filter(ImageFilter.GaussianBlur(pad / 2)), soft[:2])
    s = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x = round((im.width - W) * fx); y = (im.height - H) // 2
    im.crop((x, y, x + W, y + H)).save(os.path.join(OUT, name.split("/")[-1] + ".jpg"), quality=88)
    print(name, im.size)
