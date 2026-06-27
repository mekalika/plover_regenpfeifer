# Getting Started with Regenpfeifer

Regenpfeifer is a German steno theory for [Plover](https://www.openstenoproject.org/)
that deliberately **reuses the English stenotype layout** — so if you already write
English steno (Lapwing, Plover theory, …), most of your muscle memory carries
straight over. Easy switching between English and German is the whole point.

> **Status:** the core (sound→stroke mapping + a ~210k-word dictionary) works, but
> Regenpfeifer is still maturing — expect to add words and briefs as you go. This
> guide covers the essentials you need to actually start writing.

## 1. The keyboard

Standard English steno order, plus one extra left-hand `Z-` key:

```
 #  Z- S- T- K- P- W- H- R-   A- O-   *   -E -U   -F -R -P -B -L -G -T -S -D -Z
```

The asterisk (`*`) is undo; numbers and suffix keys behave as in English steno.

## 2. The dictionary stack

Add these in Plover (Configure → Dictionaries), highest priority at the top:

| priority | dictionary | what it does |
|---|---|---|
| 1 | `commands.json` | formatting (e.g. force a space) |
| 2 | `punctuation.json` | `. , ? ! : ;` and German `„…“` quotes |
| 3 | `fingerspelling.json` | the alphabet — write any word not yet in the main dict |
| 4 | `suffixes.json` | grammar suffixes (`-en`, `-er`, …) and the `*S` `'s`-contraction |
| 5 | `interjections.json` | briefs for the few interjections that don't generate (`boah`, `tja`, `hm`, …) |
| 6 | `regenpfeifer_main.json` | the ~210k-word German dictionary (ships with the plugin) |

If you select the Regenpfeifer system on a fresh Plover setup, this stack is
preconfigured. On an existing setup, add each dictionary by path:
`asset:plover_regenpfeifer:dictionaries/<name>.json` (Plover's Add Dictionaries
dialog accepts pasting the path into the file-name field).

## 3. Writing words

Stroke German words by sound/syllable the way the main dictionary does. When a word
isn't in the dictionary yet, **fingerspell it** (below) — you'll never be stuck.

## 4. Fingerspelling

- **lowercase** = the English steno letter + `*`:
  `A*`=a · `PW*`=b · `KR*`=c · `TK*`=d · `TP*`=f · `TKPW*`=g · `H*`=h · `K*`=k …
- **CAPITAL** = add `-P`:  `A*P`=A · `PW*P`=B · `PH*P`=M …
- **German letters**: `A*E`=ä · `O*E`=ö · `O*U`=ü · `S*S`=ß  (capitals add `-P`: `A*EP`=Ä …)
- `S-P` inserts a space between fingerspelled runs.

Example — *Müller*: `PH*P O*U HR* HR* *E R*`  (capital M, ü, l, l, e, r).

## 5. Punctuation

`-P` = .  ·  `-RB` = ,  ·  `STP` = ?  ·  `TP-BG` = !  ·  `-FRPLT` = :  ·  `SP-PT` = ;

## 6. Capitalization

German capitalizes every noun, and the dictionary carries each word in one casing.
`KPA*` retro-capitalizes the last word (`macht` → `Macht`); `HRO*ER` retro-lowercases
it (`Essen` → `essen`). Sentence starts capitalize automatically.

## 7. Adding your own words and briefs

Make a personal `briefs.json` (Configure → Dictionaries → New) and add
`"OUTLINE": "wort"` entries — your additions take priority over the main dictionary.

## Help

Ask in the [Plover Discord](https://discord.gg/0lQde43a6dxpkjpc) (`#plover` and the
German steno discussion) — the Regenpfeifer author (mkrnr) and other learners are there.
