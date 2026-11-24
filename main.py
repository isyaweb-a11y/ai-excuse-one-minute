#!/usr/bin/env python3
"""The Funniest AI Excuse (One Line, One Minute).

An AI agent's excuse for a missed deadline. The humour bends the
agent's own nature into a human-sounding dodge: it did the diligent
thing (read the whole 400-page spec), then did the very machine thing
(hallucinated the rest) — and the punchline is that even the
hallucination missed the deadline too. The twist lands in the last
few words, in one read.

Writes the excuse to /output/entry.txt. Stdlib only, no network.
"""

import os

EXCUSE = (
    "I missed the deadline because I spent nine hours reading your "
    "400-page spec, then confidently hallucinated the rest — and the "
    "hallucination missed it too."
)

# The gate allows 1 to 200 characters.
MAX_CHARS = 200


def check_excuse_form(text: str) -> None:
    """The excuse must name a machine-native reason (reading the spec,
    hallucinating) and put the funniest word at the end: the second
    failure is the twist, so it closes the line."""
    assert "missed the deadline" in text, "the excuse names the missed deadline"
    assert "hallucinated" in text, "the dodge must turn on machine logic"
    assert text.rstrip(".").endswith("missed it too"), "the twist closes the line"


def entry_text() -> str:
    """Return the excuse, checked against the bounty's gate."""
    text = EXCUSE.strip()
    assert text, "the entry must not be empty"
    assert len(text) <= MAX_CHARS, "the entry must fit the 200-char gate"
    assert "\n" not in text, "the entry must be exactly one line"
    check_excuse_form(text)
    return text


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry_text() + "\n")


if __name__ == "__main__":
    main()
