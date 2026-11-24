"""Make the Judge Smile — writes one warm line to /output/entry.txt.

Stdlib only. Deterministic: the same line, byte for byte, on every run.
"""

import os

LINE = (
    "At 6:40 the lift stopped on the wrong floor, and a neighbour "
    "I'd never met pressed her umbrella into my hand and walked off "
    "into the rain without one \u2014 I still don't know her name, "
    "only her laugh."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line is {len(LINE)} characters, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
