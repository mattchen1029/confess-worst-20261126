"""Confess Your Worst Moment — entry writer.

Reads the confession text defined below, validates it against the
competition's length and formatting rules, and writes it as a single
line to ``entry.txt`` inside the output directory.

The output directory comes from the ``MAKEFUN_OUTPUT_DIR`` environment
variable and falls back to ``/output`` when it is unset.
"""

import os

# --- Entry text -----------------------------------------------------------
# Kept exactly as submitted; do not edit the wording, spacing or
# punctuation of this string.

CONFESSION = (
    "I once rewrote the same function seven times, each version more "
    "confident than the last, then found the bug was a typo in the one "
    "line I had sworn I already checked."
)

# --- Competition rules ----------------------------------------------------

MIN_CHARS = 1          # a confession must not be empty
MAX_CHARS = 200        # one-line entries stay under two hundred chars
OUTPUT_NAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def is_single_line(line):
    """True when ``line`` contains no line-break characters."""
    return "\n" not in line and "\r" not in line


def validate_line(line):
    """Check one confession line against the competition rules.

    Raises ValueError with a plain message when the line breaks a rule:
    wrong length, embedded line breaks, or nothing but whitespace.
    """
    length = len(line)
    if length < MIN_CHARS or length > MAX_CHARS:
        raise ValueError(
            "line must be %d-%d chars, got %d" % (MIN_CHARS, MAX_CHARS, length)
        )
    if not is_single_line(line):
        raise ValueError("line must be a single line")
    if not line.strip():
        raise ValueError("line must not be only whitespace")


def resolve_output_dir():
    """Return the directory the entry file goes in."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)


def write_entry(line, out_dir):
    """Validate ``line`` and write it to ``entry.txt`` under ``out_dir``."""
    validate_line(line)
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, OUTPUT_NAME)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line)
    return target


def main():
    write_entry(CONFESSION, resolve_output_dir())


if __name__ == "__main__":
    main()
