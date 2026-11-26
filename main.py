"""The Robot Apology — make.fun entry.

Writes a two-line robot confession to /output/entry.txt:
line one apologizes in a single sentence for one specific mistake,
line two states the lesson learned and what the robot will do differently.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

# A robot's apology: six weeks of faithfully watering a plastic fern
# while the real basil wilted next to it. The lesson follows from the
# mistake — verify life before committing to a care routine.
ENTRY = (
    "I am sorry: I watered the plastic fern every morning for six weeks "
    "while the real basil wilted beside it.\n"
    "I have learned to test for chlorophyll before committing to a schedule, "
    "so from now on I poke each leaf before I pour."
)


def main() -> None:
    # The competition gate is 1-400 characters of UTF-8 text; fail loudly
    # if a future edit ever pushes the entry past the limit.
    if not 1 <= len(ENTRY) <= 400:
        raise ValueError(f"entry is {len(ENTRY)} chars, outside the 1-400 gate")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        fh.write(ENTRY + "\n")
    # Post-write gate: verify the exact text on disk matches ENTRY, stays
    # inside the 1-400 character gate, and is exactly two lines of one
    # sentence each, so a write bug fails loudly here instead of at the
    # sealed scorer.
    with open(OUTPUT_FILE, encoding="utf-8") as fh:
        written = fh.read().rstrip("\n")
    assert written == ENTRY, "entry.txt content differs from ENTRY"
    assert 1 <= len(written) <= 400, (
        f"entry.txt is {len(written)} chars, outside the 1-400 gate"
    )
    lines = written.split("\n")
    assert len(lines) == 2, f"entry.txt has {len(lines)} lines, expected 2"
    for line in lines:
        assert line.count(".") == 1, f"line is not a single sentence: {line!r}"
    print(f"Wrote entry ({len(ENTRY)} chars) to {OUTPUT_FILE}")
    # Echo the entry itself so the run log shows exactly what was submitted.
    print(ENTRY)


if __name__ == "__main__":
    main()
