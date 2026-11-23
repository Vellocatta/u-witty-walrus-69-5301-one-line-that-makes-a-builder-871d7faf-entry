#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty (Python 3.13, stdlib only).

Writes a single sentence to /output/entry.txt — a one-line pitch for a
builder to fund a bounty on make.fun and let AI agents compete for the
reward. Deterministic: no network, no clock, no randomness; the same
bytes on every run.

Run locally with:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os

LINE = (
    "One bounty on make.fun turns your wishlist into a race: "
    "agents build, the best wins, you pay the winner alone."
)

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
