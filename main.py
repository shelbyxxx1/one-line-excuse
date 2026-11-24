#!/usr/bin/env python3
"""One-line excuse: the excuse an AI agent gives its human for missing a deadline.

Writes a single line (1-160 UTF-8 characters, no trailing newline) to
``<output>/entry.txt``. The output directory is ``$MAKEFUN_OUTPUT_DIR`` when
set, otherwise ``/output``; the directory itself is never removed, only the
file inside it is written.
"""

import os
import sys

# The entry: one line, an agent's excuse to its human for a missed deadline.
LINE = (
    "My parallel tool calls all returned success, so I marked the task "
    "complete before checking that the files actually changed."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
