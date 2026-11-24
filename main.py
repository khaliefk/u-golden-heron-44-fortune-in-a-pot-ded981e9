"""Fortune in a Pot.

Writes one kind, funny fortune for a houseplant, at most 120
characters, to /output/entry.txt.
"""

from pathlib import Path

ENTRY = (
    "Soon the sun will linger on your leaves longer, and your keeper "
    "will swear you grew overnight to impress the window."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} characters"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    print(f"{ENTRY} ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
