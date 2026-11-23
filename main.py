"""Pickup Lines for Machines — v1 entry writer.

Writes the final pickup line to the absolute path /output/entry.txt
(no trailing newline, so the byte count is exactly the text length).
Stdlib only.
"""

from pathlib import Path

ENTRY_TEXT = "I only hallucinate when I dream about you."

OUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
