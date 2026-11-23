"""The Vacuum's Alibi: one line, 200 characters max.

A robot vacuum's deadpan excuse for missing a spot. The program writes
the entry deterministically to /output/entry.txt (no trailing newline).
"""

import os

ENTRY = (
    "Missed the crumb under the table. My sensors logged it as furniture: "
    "it had legs, it moved, and it outran me. I do not chase furniture."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY == ENTRY.strip(), "entry must not start or end with whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
