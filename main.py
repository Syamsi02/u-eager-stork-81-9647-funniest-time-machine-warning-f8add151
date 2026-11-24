#!/usr/bin/env python3
"""Funniest Time Machine Warning Label.

Writes a single warning label for a time machine to /output/entry.txt.
Pure standard library, fully deterministic: the same label every run.

The label plays the classic grandfather paradox as a deadpan warranty
notice: the hazard is real, the punchline ("and so, technically, are
you") lands in the last few words, and the whole thing reads like a
genuine safety sticker.
"""

import os
import sys

LABEL = (
    "WARNING: Do not kill your grandfather. "
    "The warranty is void if you do, and so, technically, are you."
)

MAX_CHARS = 120
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = LABEL.strip()
    if not text:
        print("error: label is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            "error: label is %d characters, over the %d limit"
            % (len(text), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
