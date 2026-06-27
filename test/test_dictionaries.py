"""Sanity checks for every shipped dictionary.

Pure stdlib on purpose: valid JSON, no duplicate keys, every stroke in
Regenpfeifer steno order, and no outline collisions inside the default stack.
"""
import json
import re
from collections import Counter
from pathlib import Path

DICT_DIR = Path(__file__).parent.parent / "plover_regenpfeifer" / "dictionaries"
SYSTEM = Path(__file__).parent.parent / "plover_regenpfeifer" / "system.py"


def _system_attrs():
    namespace = {}
    exec(SYSTEM.read_text(), namespace)
    return namespace


_NS = _system_attrs()
KEYS = _NS["KEYS"]
DEFAULT_DICTIONARIES = _NS["DEFAULT_DICTIONARIES"]

LEFT = [k[:-1] for k in KEYS if k.endswith("-")]
MIDS = [k for k in KEYS if not k.endswith("-") and not k.startswith("-") and k != "#"]
RIGHT = [k[1:] for k in KEYS if k.startswith("-")]
CANON = LEFT + MIDS + RIGHT


def valid_stroke(stroke):
    if not stroke or re.search(r"\d", stroke):
        return False
    pointer = 0
    for ch in stroke:
        if ch == "-":
            pointer = max(pointer, len(LEFT) + len(MIDS))
            continue
        j = pointer
        while j < len(CANON) and CANON[j] != ch:
            j += 1
        if j == len(CANON):
            return False
        pointer = j + 1
    return True


def load_pairs(path):
    return json.loads(path.read_text(encoding="utf8"), object_pairs_hook=list)


def all_dictionaries():
    return sorted(DICT_DIR.glob("*.json"))


def test_dictionaries_exist():
    assert all_dictionaries(), f"no dictionaries in {DICT_DIR}"
    names = {p.name for p in all_dictionaries()}
    assert set(DEFAULT_DICTIONARIES) <= names


def test_valid_json_no_duplicate_keys():
    for path in all_dictionaries():
        pairs = load_pairs(path)
        duplicates = [k for k, n in Counter(k for k, _ in pairs).items() if n > 1]
        assert not duplicates, f"{path.name}: duplicate keys {duplicates[:5]}"


def test_every_stroke_in_steno_order():
    for path in all_dictionaries():
        bad = [
            outline
            for outline, _ in load_pairs(path)
            for stroke in outline.split("/")
            if not valid_stroke(stroke)
        ]
        assert not bad, f"{path.name}: invalid strokes {bad[:5]}"


def test_default_stack_collision_free():
    seen = {}
    clashes = []
    for name in DEFAULT_DICTIONARIES:
        for outline, word in load_pairs(DICT_DIR / name):
            if outline in seen and name != seen[outline][0]:
                clashes.append((outline, seen[outline], (name, word)))
            seen.setdefault(outline, (name, word))
    assert not clashes, f"stack collisions: {clashes[:5]}"
