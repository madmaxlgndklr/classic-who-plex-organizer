import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from organize_classic_who import build_plan, _ep_dest, _extras_dest, SERIALS, SPECIALS


def test_build_plan_empty():
    assert build_plan([], []) == []


def test_ep_dest_format():
    p = _ep_dest(1, 1, "An Unearthly Child", False)
    assert p.name == "Doctor Who (1963) - S01E01 - An Unearthly Child.avi"
    assert "Season 01" in str(p)


def test_ep_dest_recon():
    p = _ep_dest(1, 14, "The Roof of the World", True)
    assert p.name == "Doctor Who (1963) - S01E14 - The Roof of the World (Recon).avi"


def test_extras_dest_format():
    p = _extras_dest(5, "bonus.avi")
    assert "Season 05" in str(p)
    assert "extras" in str(p)
    assert p.name == "bonus.avi"


def test_all_plan_entries_are_path_tuples():
    moves = build_plan(SERIALS, SPECIALS)
    for src, dest in moves:
        assert isinstance(src, Path), f"src not Path: {src}"
        assert isinstance(dest, Path), f"dest not Path: {dest}"


def test_no_duplicate_destinations():
    moves = build_plan(SERIALS, SPECIALS)
    dests = [str(d) for _, d in moves]
    dupes = [d for d in dests if dests.count(d) > 1]
    assert not dupes, f"Duplicate destinations: {set(dupes)}"
