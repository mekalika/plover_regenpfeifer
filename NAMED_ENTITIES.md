# Named entities — cities, countries, surnames

Proper nouns are mostly missing from the generated dictionary because they were
never in the wortformliste *input* — not because they can't be generated. Once the
generator runs (it needs the validator fix in the `regenpfeifer` repo to produce
anything on modern Python), regular German-spelled names and places generate
cleanly. This is a small, opt-in supplement for them.

- **`named_entities.csv`** — a curated list of ~130 countries, German/world cities,
  and common surnames, in wortformliste format (`Name,sg`). Add it to the
  generator's input and the next regeneration makes these *writable* instead of
  fingerspelled. This is the durable contribution.
- **`dictionaries/named_entities.json`** (93) — the generated outlines, usable now:
  `Berlin` `PWER/HREUPB`, `München` `PHOUPB/KHEPB`, `Deutschland` `TKOEUT/SHRAPBD`,
  and — since the schm/schn onsets landed — `Schmidt` `SPHEUTD`.
- **`dictionaries/briefs_named_entities.json`** (40) — one-stroke folds for the
  multi-stroke ones, collision-free against the whole stack: `Berlin`→`PWERPB`,
  `Stuttgart`→`STUT`, `Moskau`→`PHOS`.

Useful anywhere proper nouns are constant — court/legal, news, transcription.

**Where the rest of the csv went** (~130 rows → 93 outlines):

- **Already writable in the main dictionary** — `Weber`, `Koch`, `Stein`, `Kaiser`,
  `Fischer`, `Müller`, `König`, `Schneider`, `Russland`, `Schweden`, … double as
  ordinary German words, so the generator already covers them (~19 names).
- **Collision losers** — some names generate exactly one outline and a more common
  word owns it: `Braun`/`braun`, `Klein`/`klein`, `Bonn`/`Bon`. Those get the
  homophone-style `*`-marked form here (`PWRA*UPB`, `KHRA*EUPB`, `PWO*PB`). `Roth`
  and `Frank` stay out — their starred forms belong to the more common `Rot`/`fragen`
  disambiguations — fingerspell them or add a personal brief.
- **Foreign spellings** (`Italien`, `Stockholm`) need the pronunciation channel that
  German orthography can't supply. They're listed in `named_entities.csv` regardless,
  so they're covered once that path lands.
