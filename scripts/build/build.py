"""Build generated pages. Usage (from repo root): python scripts/build/build.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

import gen_static  # noqa: E402

STEPS = [gen_static.build]
for mod in ("gen_pages", "gen_home", "postprocess"):
    try:
        STEPS.append(__import__(mod).build)
    except ModuleNotFoundError:
        pass

if __name__ == "__main__":
    for step in STEPS:
        step()
        print("built", step.__module__)
