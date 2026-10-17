"""Export the site for the dhakaad.com root (Hostinger).

The repository serves from /dhaka-ad-website/ on GitHub Pages; the live domain
serves from /. This copies the site to OUT with root-relative paths, adds the
Apache/LiteSpeed config and legacy files the old dhakaad.com used.

Usage: python scripts/build/export_domain.py [OUT]   (default: _site)
"""
import os
import shutil
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SKIP_DIRS = {".git", ".github", "scripts", "_site", "node_modules", "promo"}
SKIP_FILES = {"README.md", ".gitignore", ".nojekyll"}
TEXT = (".html", ".css", ".js", ".xml", ".txt", ".json")

HOSTINGER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hostinger")


def main(out):
    out = os.path.abspath(out)
    if os.path.exists(out):
        shutil.rmtree(out)
    for d, dirs, files in os.walk(ROOT):
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
        rel = os.path.relpath(d, ROOT)
        target_dir = os.path.join(out, rel) if rel != "." else out
        os.makedirs(target_dir, exist_ok=True)
        for f in files:
            if f in SKIP_FILES:
                continue
            src, dst = os.path.join(d, f), os.path.join(target_dir, f)
            if f.endswith(TEXT):
                with open(src, encoding="utf-8") as fh:
                    text = fh.read()
                with open(dst, "w", encoding="utf-8") as fh:
                    fh.write(text.replace("/dhaka-ad-website/", "/"))
            else:
                shutil.copy2(src, dst)
    # Server rules (legacy WordPress 301s, PHP lockdown, https), the callback mailer,
    # the staging robots file and the old /img/ URLs that redirects and shares point at.
    shutil.copy2(os.path.join(HOSTINGER, "htaccess"), os.path.join(out, ".htaccess"))
    for f in ("contact.php", "robots-staging.txt"):
        shutil.copy2(os.path.join(HOSTINGER, f), os.path.join(out, f))
    shutil.copytree(os.path.join(HOSTINGER, "img"), os.path.join(out, "img"))
    # Files the previous dhakaad.com exposed, so old links and shares keep working.
    shutil.copy2(os.path.join(ROOT, "assets", "dhaka-ad-favicon-red.png"), os.path.join(out, "favicon.png"))
    shutil.copy2(os.path.join(ROOT, "assets", "apple-touch-icon.png"), os.path.join(out, "apple-touch-icon.png"))
    og = os.path.join(ROOT, "assets", "outdoor", "dhaka-city-user-hero.webp")
    try:
        from PIL import Image
        Image.open(og).convert("RGB").save(os.path.join(out, "assets", "og.jpg"), quality=85)
    except ImportError:
        pass
    leftovers = []
    for d, _dirs, files in os.walk(out):
        for f in files:
            if f.endswith(TEXT) and "/dhaka-ad-website" in open(os.path.join(d, f), encoding="utf-8").read():
                leftovers.append(os.path.join(d, f))
    if leftovers:
        sys.exit(f"base path left in {len(leftovers)} files, e.g. {leftovers[:3]}")
    print("exported to", out)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "_site"))
