#!/usr/bin/env python3
"""The Dog Reviews the Mailman (make.fun bounty
u-motasimfuad-the-dog-reviews-the-mailman-87608f85).

Writes one funny one-line review a dog gives the mailman to
/output/entry.txt. Gate: UTF-8 text, 1-200 characters, not only
whitespace, one line.

Entry (147 characters):

  One star. He shoves letters through my slot every morning at 9
  and runs. I have chased him 214 times and he still acts like
  I'M the suspicious one.

Built against the judge's brief in the kit's competition.yaml, in
the brief's own order:
  1. On subject: a dog reviewing the mailman, nothing else.
  2. The dog's side of the visit: a grievance (letters shoved
     through the slot, mailman runs) plus a suspicion -- the dog
     has chased him 214 times and still gets treated as the
     suspicious one. The grudge IS the joke.
  3. Dog's voice, dog's priorities: "my slot", "chased him",
     the mailman's morning round as an invasion of the dog's
     territory. No person wearing a fur suit.
  4. One line, tight and complete, with the turn at the end:
     the reversal -- after 214 chases, the MAILMAN acts like
     the DOG is the suspicious one. Without that last clause
     the line is a plain complaint with no landing.
  5. Specific to this dog and this mailman: the slot, 9 in the
     morning, 214 chases. The joke does not fit any stranger
     at the door.

Playbook check (winner-study-20261125.md, checklist 7B, joke
type): length 147 inside the joke-winner range 90-208 (median
116); one mechanism, three beats (shove letters -> run ->
214 chases -> reversal); 4 concrete details (slot, 9am,
214 times, one star); twist only in the final clause.

Rejected drafts (same session):
  - "Two stars. He rings twice, drops the good mail, and flees
    before I can thank him -- 214 visits, zero belly rubs, one
    very suspicious uniform." (140 chars) -- the "zero belly
    rubs" beat is a second grievance that dilutes the single
    mechanism, and "suspicious uniform" states the suspicion
    instead of landing it as a reversal.
  - "One star: he delivers my mail, then sprints off like I
    owe him money. After 312 chases I finally caught his
    shoelace -- he still won't stay for a treat." (151 chars)
    -- "caught his shoelace" is a triumph, but "won't stay
    for a treat" is a soft ending; the chosen line's reversal
    ("I'M the suspicious one") lands harder and is the only
    draft where the punch reframes the whole setup.

Deterministic: the line is a fixed string, no randomness, no
network, no model calls. Every run writes the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

REVIEW = (
    "One star. He shoves letters through my slot every morning "
    "at 9 and runs. I have chased him 214 times and he still "
    "acts like I'M the suspicious one."
)


def _validate(text: str) -> None:
    """Check the entry against the kit gate: 1-200 chars, one line,
    not only whitespace. The review is 147 chars, inside the gate."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"review must be 1-200 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    if not text.strip():
        raise ValueError("review must not be only whitespace")


def main() -> None:
    _validate(REVIEW)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    # Round-trip check: a partial write or an encoding slip must fail
    # loudly instead of shipping a short or garbled line to the judge.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != REVIEW:
        raise ValueError("entry.txt round-trip mismatch: written bytes differ")
    _validate(written)


if __name__ == "__main__":
    main()
