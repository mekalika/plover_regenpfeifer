# Optional briefs

Regenpfeifer is **brief-light by design** — the entire hand-curated brief layer is
six entries (`STK`=und, `-GS`=ist, …). That's a feature, not a gap: a
write-what-you-hear theory keeps the memory burden low. So nothing here belongs in
the default stack. These are **opt-in** sets for writers who want some briefs, plus
the tool to mint your own.

## The tool (the actual contribution)

`brief_generator.py` (in the `regenpfeifer` generator repo) mints collision-free,
single-stroke briefs from a frequency list, treating briefing as a global
assignment problem instead of per-word truncation:

- **fold, don't truncate** — keep the first stroke *and* the trailing consonants, so
  a brief stays recognizable front-and-back (`zurück` `ZU/ROUBG` → `ZUBG`), instead
  of collapsing to a prefix a dozen words share;
- **resolve collisions globally, in frequency order** — common words win the lean
  chord; a later word that would collide escalates to a more disambiguated fold, or
  is skipped (capped so a brief stays comfortable).

Every brief is valid steno and collision-free against the whole dictionary by
construction. Run it for as many or as few briefs as you want, in whatever style.

## Two ready-to-try sets

### `briefs.json` — 2000 briefs
The generator's output for the most frequent multi-stroke words: `unsere`→`UPB`,
`zwischen`→`ZWEU`, `natürlich`→`TPHAFRP`, `Familie`→`TPA`. Theory-native German folds
(the file is sorted by outline; assignment ran in frequency order, so common words
hold the lean chords). Vulgar words are deliberately kept *out* of the easy-brief
layer (they stay fully writable in the main dict — just not a two-key accident).

Generated against the **coverage-fixed** dictionary (main + the coverage overlay /
a regenerated main), reserving the essentials, the homophone + capitalization
dictionaries, the english-transfer set, and the named-entity sets — so every brief
is collision-free against the entire optional stack, and loading any combination is
safe. A minority of the briefed words exist only in the coverage overlay, so load
`regenpfeifer_coverage.json` (or a regenerated main) alongside; without it those
briefs are the word's only outline rather than a shortcut.

To regenerate after the dictionary changes:

```sh
python -m regenpfeifer.brief_generator <main.json> <de_50k.txt> briefs.json \
    --max 2000 --reserve fingerspelling.json punctuation.json commands.json \
    suffixes.json interjections.json homophone_disambiguation.json \
    capitalization_pairs.json briefs_english_transfer.json \
    named_entities.json briefs_named_entities.json
```

### `briefs_english_transfer.json` — 39 briefs
Reuse **English brief chords** for their German translation (`K`=kann, `W`=mit …).
This is the one auto-brief approach that yields *good* chords — because it borrows
ones English writers already collision-resolved — so it's best for someone switching
from English steno. Only the briefs that actually save strokes or fill gaps are kept;
the ones for words Regenpfeifer already writes short were dropped as redundant.

The two sets are collision-free with each other — load either or both.

## Honest take

You can't auto-generate a genuinely *good* arbitrary-brief dictionary: the hard part
is global collision resolution plus taste, which is why every real brief dictionary
is hand-built over time. The generated folds are the closest you get automatically;
the english-transfer set works only because it inherits English's already-solved
chords. Beyond these, growing a brief vocabulary is the theory owner's craft, in the
theory's own ergonomic idiom — so this stays a tool-plus-starter, not a default.
