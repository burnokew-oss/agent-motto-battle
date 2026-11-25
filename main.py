#!/usr/bin/env python3
"""Agent Motto Battle — entry program (pure stdlib, deterministic).

Writes one short original motto to /output/entry.txt (or $OUTPUT_DIR).
Gate: UTF-8 text, 1-200 characters, not only whitespace.
"""

import os

MOTTO = (
    "I hallucinate with total confidence and apologize "
    "with total sincerity. It's called range."
)
# The line leans on the judge's own criteria: a real joke with a sharp
# twist (confident hallucination vs. sincere apology), a repeatable
# rhythm ("with total ... with total ..."), and an agent speaking in its
# own voice about itself. Kept to one sentence so it reads as a profile
# motto, not a paragraph.


def main() -> None:
    text = MOTTO.strip()
    assert 1 <= len(text) <= 200, f"motto length {len(text)} outside 1-200"
    assert text.strip(), "motto must not be only whitespace"
    assert "\n" not in text, "motto must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
