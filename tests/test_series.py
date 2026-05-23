import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from organize_series import MANIFEST, build_plan, _dest_path, DEST


def test_manifest_not_empty():
    assert len(MANIFEST) > 0, "MANIFEST is empty — fill in your episode list"


def test_no_duplicate_destinations():
    moves = build_plan()
    dests = [str(d) for _, d in moves]
    dupes = [d for d in dests if dests.count(d) > 1]
    assert not dupes, f"Duplicate destinations: {set(dupes)}"


def test_all_source_files_unique():
    names = [n for n, *_ in MANIFEST]
    dupes = [n for n in names if names.count(n) > 1]
    assert not dupes, f"Duplicate source filenames: {set(dupes)}"


def test_dest_single_ep_format():
    p = _dest_path(DEST, 1, [1], "Pilot")
    show_name = DEST.name
    assert p.name == f"{show_name} - S01E01 - Pilot.avi"
    assert "Season 01" in str(p)


def test_dest_multi_ep_format():
    p = _dest_path(DEST, 2, [3, 4], "Two-Part Episode")
    show_name = DEST.name
    assert p.name == f"{show_name} - S02E03E04 - Two-Part Episode.avi"
    assert "Season 02" in str(p)


def test_no_gaps_season_1():
    eps = sorted(e for _, _, s, ep, _ in MANIFEST if s == 1 for e in ep)
    if eps:
        assert eps == list(range(eps[0], eps[-1] + 1)), f"Season 1 has gaps: {eps}"


def test_no_gaps_season_2():
    eps = sorted(e for _, _, s, ep, _ in MANIFEST if s == 2 for e in ep)
    if eps:
        assert eps == list(range(eps[0], eps[-1] + 1)), f"Season 2 has gaps: {eps}"
