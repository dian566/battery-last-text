#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the battery's farewell text to its charger into /output/entry.txt.

The program emits exactly one line of at most 199 characters and appends
no trailing newline, as the make.fun bounty requires.
"""

from pathlib import Path

TEXT = (
    "I waited all day at 1% while you flirted with every other phone. "
    "This is my goodbye text — I'm leaving you for a power bank who actually shows up."
)
DESTINATION = Path("/output/entry.txt")


MAX_LENGTH = 199


def build_entry() -> str:
    message = TEXT.strip()
    size = len(message)
    if size < 1 or size > MAX_LENGTH:
        raise ValueError(f"entry length {size} is outside the 1-{MAX_LENGTH} range")
    if "\n" in message or "\r" in message:
        raise ValueError("entry must be exactly one line")
    return message


def run() -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(build_entry(), encoding="utf-8", newline="")


if __name__ == "__main__":
    run()
