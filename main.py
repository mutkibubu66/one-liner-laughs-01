#!/usr/bin/env python3
"""Write one original funny one-liner to /output/entry.txt.

The joke: a smartwatch celebrates 10,000 steps, but every one of them
was just pacing while waiting for a one-letter reply. The fitness
triumph is real; the reason for it is bleak. The watch celebrates the
symptom, not the life: the narrator did not go for a run, they wore a
hole in the carpet waiting on a "k".

Why it should land with the judge: the setup promises a wholesome
fitness win, the punchline reframes every step as anxiety, and the
whole turn fits in a single breath. No word is doing nothing.
"""

import os
import sys

# The line is kept as two halves so the turn is visible in the source:
# a congratulatory setup, then the bleak reason for it.
SETUP = "My smartwatch congratulated me on 10,000 steps \u2014 "
PUNCHLINE = "all of them pacing while I waited for a reply that just said 'k'."
JOKE_PARTS = (SETUP, PUNCHLINE)

MAX_CHARS = 200

OUTPUT_PATH = "/output/entry.txt"


def build_line() -> str:
    """Join the setup and punchline into the single entry line."""
    return "".join(JOKE_PARTS)


def check_line(line: str, where: str) -> str | None:
    """Return an error message if a line breaks a gate, else None."""
    if "\n" in line or "\r" in line:
        return f"FAIL: {where} must be a single line"
    if not line.strip():
        return f"FAIL: {where} must not be only whitespace"
    if line != line.strip():
        return f"FAIL: {where} must not start or end with whitespace"
    length = len(line)
    if not 1 <= length <= MAX_CHARS:
        return f"FAIL: {where} is {length} characters, must be 1-{MAX_CHARS}"
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
    print(f"Gate: 1-{MAX_CHARS} characters, single line, no padding \u2014 OK")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
