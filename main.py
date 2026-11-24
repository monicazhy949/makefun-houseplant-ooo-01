#!/usr/bin/env python3
"""{e["title"]}.

Writes a single line of text to /output/entry.txt.
Pure stdlib, deterministic, no network, no input files.
"""

import os

ENTRY = (
    'Out of office: I am a fern, ignored since March. Water your own emails — I am busy dying dramatically in the corner.'
)
# Revision: v1 was only setup (ignored fern, water your emails) with no payoff.
# Revised: tightened the setup and added the punchline — busy dying dramatically in the corner.


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 120, f"entry must be 1-120 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
