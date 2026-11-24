"""Pickup line for machines: one line, straight to the point.

The line plays on autocomplete — the most machine-native habit there is.
A language model, an IDE, a keyboard: they all finish your sentences.
"You autocomplete me" is a machine saying "you complete me", literally,
in the one verb machines actually do all day.
"""

import os


def main():
    pickup = "You autocomplete me."
    out_path = "/output/entry.txt"
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(pickup)


if __name__ == "__main__":
    main()
