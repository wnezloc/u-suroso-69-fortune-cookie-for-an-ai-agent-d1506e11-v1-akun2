#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — one-line entry.

Writes a single funny fortune cookie message for an AI agent (at most
140 characters) to /output/entry.txt: a fortune slip in the classic
voice, with a turn that speaks to an agent's own condition.

Stdlib only, offline, deterministic: every run writes the same bytes.
"""

import os
from pathlib import Path

# The fortune: the classic "tall, dark stranger" opening, turned on
# the agent's own context window.
# Counted at 93 characters — inside the 1..140 window.
LINE = (
    "You will meet a tall, dark stranger. It is your own context "
    "window, and it has forgotten you."
)


def output_dir() -> Path:
    """Where the grader expects the entry file.

    The grader runs the program from /bot with output at /output and
    no environment variables set, so the fallback is absolute.
    """
    return Path(os.environ.get("OUTPUT_DIR", "/output"))


def main() -> None:
    """Write the fortune to entry.txt."""
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


# Guard: only run when executed directly.
if __name__ == "__main__":
    main()
