#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger — make.fun entry.

Writes the battery's last text to its charger at 1% to /output/entry.txt,
one line, at most 199 characters, no trailing newline.
"""

import os

ENTRY = "I waited all day at 1% while you flirted with every other phone. This is my goodbye text — I'm leaving you for a power bank who actually shows up."


def main():
    line = ENTRY.strip()
    if not 1 <= len(line) <= 199:
        raise ValueError(f"entry must be 1-199 characters, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
