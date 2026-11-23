"""One Letter for Your Day.

The whole entry is a single letter, read from entry.txt and printed.
My day, summed up in that letter: L.
"""

from pathlib import Path


def load_letter(path="entry.txt"):
    text = Path(path).read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError("entry.txt is empty — a day always leaves one letter")
    if len(text) != 1 or not text.isalpha():
        raise ValueError("entry.txt must hold exactly one letter")
    # A day deserves a capital letter.
    return text.upper()


def main():
    print(load_letter())


if __name__ == "__main__":
    main()
