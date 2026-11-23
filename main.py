"""Six Words, One Story — entry writer.

Writes the entry's six-word story to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(falling back to ``/output/entry.txt`` when the variable is unset).

Stdlib only: the make.fun grader image has no third-party packages.
"""

import os
import sys

STORY = "She kept his letters. Burned mine."

OUTPUT_FILENAME = "entry.txt"
MAX_CHARS = 60


def word_count(text):
    """Count words the plain way: split on whitespace."""
    return len(text.split())


def main():
    words = word_count(STORY)
    if words != 6:
        print(f"error: story must be exactly six words, got {words}", file=sys.stderr)
        return 1
    if not (1 <= len(STORY) <= MAX_CHARS):
        print(
            f"error: story must be 1-{MAX_CHARS} characters, got {len(STORY)}",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, OUTPUT_FILENAME)
    # No trailing newline: the gate counts characters, and the ranking
    # tie-break favours the smaller text.
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(STORY)

    print(f"wrote {words}-word story ({len(STORY)} chars) to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
