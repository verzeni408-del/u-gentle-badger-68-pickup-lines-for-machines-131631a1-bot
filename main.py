"""Pickup Lines for Machines — v2 entry writer (angle: autocomplete).

Writes the final pickup line to the absolute path /output/entry.txt
(no trailing newline, so the byte count is exactly the text length).
Stdlib only.
"""

from pathlib import Path

ENTRY_TEXT = "You autocomplete me."

OUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
