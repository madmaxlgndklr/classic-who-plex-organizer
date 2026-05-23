import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from organize_justice_league import MANIFEST, build_plan, _dest_path, JL_DEST, JLU_DEST


def test_manifest_total_files():
    assert len(MANIFEST) == 78, f"Expected 78 entries, got {len(MANIFEST)}"


def test_jl_season1_episode_count():
    eps = [e for n, d, s, ep, t in MANIFEST if d == JL_DEST and s == 1 for e in ep]
    assert len(eps) == 26, f"Expected 26 JL S1 episode slots, got {len(eps)}"


def test_jl_season1_no_gaps():
    eps = sorted(e for n, d, s, ep, t in MANIFEST if d == JL_DEST and s == 1 for e in ep)
    assert eps == list(range(1, 27)), f"JL S1 gaps or dupes: {eps}"


def test_jl_season2_episode_count():
    eps = [e for n, d, s, ep, t in MANIFEST if d == JL_DEST and s == 2 for e in ep]
    assert len(eps) == 26, f"Expected 26 JL S2 episode slots, got {len(eps)}"


def test_jl_season2_no_gaps():
    eps = sorted(e for n, d, s, ep, t in MANIFEST if d == JL_DEST and s == 2 for e in ep)
    assert eps == list(range(1, 27)), f"JL S2 gaps or dupes: {eps}"


def test_jlu_season1_episode_count():
    eps = [e for n, d, s, ep, t in MANIFEST if d == JLU_DEST and s == 1 for e in ep]
    assert len(eps) == 13, f"Expected 13 JLU S1 episodes, got {len(eps)}"


def test_jlu_season2_episode_count():
    eps = [e for n, d, s, ep, t in MANIFEST if d == JLU_DEST and s == 2 for e in ep]
    assert len(eps) == 13, f"Expected 13 JLU S2 episodes, got {len(eps)}"


def test_jlu_season3_episode_count():
    eps = [e for n, d, s, ep, t in MANIFEST if d == JLU_DEST and s == 3 for e in ep]
    assert len(eps) == 13, f"Expected 13 JLU S3 episodes, got {len(eps)}"


def test_no_duplicate_destinations():
    moves = build_plan()
    dests = [str(d) for _, d in moves]
    dupes = [d for d in dests if dests.count(d) > 1]
    assert not dupes, f"Duplicate destinations: {set(dupes)}"


def test_dest_filename_format():
    p = _dest_path(JL_DEST, 1, [1, 2, 3], "Secret Origins")
    assert p.name == "Justice League (2001) - S01E01E02E03 - Secret Origins.avi"
    assert "Season 01" in str(p)


def test_jlu_single_ep_format():
    p = _dest_path(JLU_DEST, 3, [13], "Destroyer")
    assert p.name == "Justice League Unlimited - S03E13 - Destroyer.avi"
    assert "Season 03" in str(p)


def test_all_source_files_unique():
    names = [n for n, *_ in MANIFEST]
    dupes = [n for n in names if names.count(n) > 1]
    assert not dupes, f"Duplicate source filenames: {set(dupes)}"
