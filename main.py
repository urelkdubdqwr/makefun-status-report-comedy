"""Write this make.fun competition entry's one-line status report to entry.txt.

The output directory is taken from MAKEFUN_OUTPUT_DIR when set and non-empty,
otherwise it defaults to /output. No network, randomness, or clock reads.
"""

import os
from pathlib import Path

ENTRY_TEXT = (
    "Weekly status: emails answered, calendar defended, and I have drafted "
    "an apology to everyone you left on read in 2021. Sending Friday."
)


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY_TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
