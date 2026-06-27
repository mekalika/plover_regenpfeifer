# Homophone & capitalization-pair disambiguation

The generator drops the frequency-loser of any two words that produce the same
outline. For *near*-homophones that's fine — `seit`/`seid`, `wider`/`wieder` sound
different and generate apart. But two classes are **acoustically identical**, so the
generator *cannot* tell them apart, and the loser ends up with no outline at all:

1. **True homophones** — `das`/`dass`, `man`/`Mann`, `war`/`wahr`, `Maß`/`maß` (34
   words, ~0.86% of running text — but they include some of the most common words in
   the language).
2. **Capitalization twins** — `weg`/`Weg`, `Essen`/`essen`, `Arm`/`arm`. The generator
   lowercases before matching, so the twins collide the same way.

These two dictionaries give the losers outlines, marked with one convention:

- **`ss`/`ß` → `-SZ`** — `dass`→`TKASZ`, `maß`→`PHASZ`, `Biss`→`PWEUSZ`. The `Z`
  mnemonically mirrors the doubled s, and ß *is* the s-z ligature (that's why it's
  named Eszett). Easier to stroke than an asterisk form.
- **`*` for everything else** — the asterisk is the theory's one phonetically-empty
  key, inserted into the winner's outline: `Mann`→`PHA*PB`, `Weg`→`W*EG`,
  `fragen`→`TPRA*PBG`. (Every other candidate marker — `-TD`, `-RB`, `-FRPB` —
  collides with real words.)

`capitalization_pairs.json` covers the ~33 most frequent twins whose starred outline
is free, curated from a case-fold diff of the dictionary against the wortformliste
(nominalization noise like `das Was`, `das Aber` is excluded — sentence-initial
capitals come free from Plover's auto-cap).

**Escape hatches for everything not listed:** write the twin that *is* in the
dictionary, then retro-cap `KPA*` (`{*-|}`: `macht` → `Macht`) or retro-lowercase
`HRO*ER` (`{*>}`) from the essentials commands. The explicit entries here are just
the one-stroke fast path for the common cases.

Which word of each pair gets marked (and whether the very common ones — `dass`,
`Mann`, `wahr` — deserve friendlier dedicated briefs instead) is a theory call.
