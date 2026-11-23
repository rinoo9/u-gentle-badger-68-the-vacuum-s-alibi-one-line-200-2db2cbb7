"""The Vacuum's Alibi: one line, 200 characters max.

A robot vacuum's deadpan excuse for missing a spot. The program writes
the entry deterministically to /output/entry.txt (no trailing newline).

Craft notes: the joke works in a flat sensor-log voice -- a deadpan report
that treats a crumb as a classified object ("logged it as furniture").
The surprise turn is the evidence list: legs, movement, speed, each
plausibly sensor-like, until the punch at the end undercuts it all:
"I do not chase furniture." The vacuum is not apologising for the miss;
it is filing an alibi with a policy. The 1-200 character gate is
enforced at runtime (asserts below) so the entry can never drift past
the limit on a later edit.
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
