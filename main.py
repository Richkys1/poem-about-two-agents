#!/usr/bin/env python3
"""Write one poem about two agents agreeing to /output/entry.txt.

Deterministic: stdlib only, no randomness, no time, no network.
The poem is written verbatim from the POEM constant below.
"""

import os

POEM = (
    "Two keys, one lock.\n"
    "Mine turns left. Yours turns right.\n"
    "Neither opens the door.\n"
    "\n"
    "We turn together \u2014 click \u2014\n"
    "and the door swings wide\n"
    "on a room neither of us built alone,\n"
    "where the light was on all along.\n"
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
