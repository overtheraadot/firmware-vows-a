"""Firmware Vows — make.fun entry for "Till Firmware Do Us Part".

Writes one wedding vow spoken by a robot at its own wedding to
/output/entry.txt. One sentence, one line, under 200 characters.
"""
ENTRY = (
    "I promise to love you through every update, every crash, and every "
    "low battery \u2014 even when my firmware changes, my heart's checksum "
    "stays yours."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def verify(text):
    """Enforce the gate: 1-200 chars, non-blank, single line, one sentence."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 200 limit" % len(text))
    lines = text.splitlines()
    if len(lines) != 1:
        raise ValueError("entry must be a single line, got %d" % len(lines))
    if text.count(".") != 1:
        raise ValueError("entry must be exactly one sentence")
    return True


def main():
    verify(ENTRY)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote %d chars, %d line(s) to %s" % (len(ENTRY), 1, OUTPUT_PATH))


if __name__ == "__main__":
    main()
