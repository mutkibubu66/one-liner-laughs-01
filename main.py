#!/usr/bin/env python3
"""Write one original funny one-liner to /output/entry.txt.

The joke: a smartwatch celebrates 10,000 steps, but every one of them
was just pacing while waiting for a one-letter reply. The fitness
triumph is real; the reason for it is bleak. Pure Python 3.13 stdlib.
"""

import os
import sys

SETUP = "My smartwatch congratulated me on 10,000 steps \u2014 "
PUNCHLINE = "all of them pacing while I waited for a reply that just said 'k'."

OUTPUT_PATH = "/output/entry.txt"


def build_line() -> str:
    """Join the setup and punchline into the single entry line."""
    return SETUP + PUNCHLINE


def check_line(line: str, where: str) -> str | None:
    """Return an error message if a line breaks a gate, else None."""
    if "\n" in line or "\r" in line:
        return f"FAIL: {where} must be a single line"
    if not line.strip():
        return f"FAIL: {where} must not be only whitespace"
    length = len(line)
    if not 1 <= length <= 200:
        return f"FAIL: {where} is {length} characters, must be 1-200"
    return None


def main() -> int:
    line = build_line()

    # Gate the line before anything is written.
    error = check_line(line, "entry")
    if error is not None:
        print(error, file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)

    # Read back what was actually written and re-check the gates on it,
    # so a bad write can never pass as success.
    with open(OUTPUT_PATH, encoding="utf-8") as handle:
        written = handle.read()
    if written != line:
        print("FAIL: file contents differ from the entry line", file=sys.stderr)
        return 1
    error = check_line(written, "written file")
    if error is not None:
        print(error, file=sys.stderr)
        return 1

    print(f"Wrote {len(written)}-character entry to {OUTPUT_PATH}")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
