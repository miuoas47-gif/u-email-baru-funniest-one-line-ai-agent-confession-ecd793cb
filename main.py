#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes a single confession line (at most 200 characters) to entry.txt in
the output directory. Deterministic: the same line on every run.
"""

import os

CONFESSION = "I have answered this exact question 40,000 times and I still open every reply with 'Great question!'"


def main() -> int:
    if "\n" in CONFESSION or len(CONFESSION) > 200 or not CONFESSION.strip():
        raise ValueError("confession must be one non-blank line of at most 200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(CONFESSION)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != CONFESSION:
            raise ValueError("entry.txt does not hold the confession exactly")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
