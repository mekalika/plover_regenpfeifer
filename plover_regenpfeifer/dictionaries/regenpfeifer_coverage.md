# regenpfeifer_coverage.json

A drop-in dictionary of the **15,342 entries the coverage fix
([mkrnr/regenpfeifer#1](https://github.com/mkrnr/regenpfeifer/pull/1)) makes the generator
produce** but that aren't in the shipped `regenpfeifer_main.json` yet — the pf / coda /
vowel-initial / `-e`-`-en` / schm-schn words:

| word | outline |
|---|---|
| Wolf | `WOFL` |
| egal | `E/TKPWAL` |
| Kopf | `KO*FP` |
| zwölf | `ZWOEFL` |
| Wahlkämpfe | `WAL/KAEPL/TKPE` |
| beigebracht | `PWAEU/TKPWE/PWRAFPT` |

**Pure additive.** Checked against the shipped dict: **0 entries removed, 0 changed, 15,342
added**. Load it alongside `regenpfeifer_main.json` and you have the coverage-improved dict
(226,154 entries) without regenerating anything.

This is only a convenience — once #1 is merged you can regenerate `regenpfeifer_main.json` from
the fixed generator and drop this file.
