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


# --- TASK 2: Season 00 / Specials ---

def test_specials_season00_count():
    from organize_classic_who import SPECIALS
    ep_nums = [e for entry in SPECIALS for (_, e, _, _) in entry["episodes"]]
    assert ep_nums == list(range(1, 8)), f"Expected S00E01-07, got {ep_nums}"


# --- TASK 3: Season 01 ---

def test_season01_episode_count():
    from organize_classic_who import SERIALS
    s1 = [e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 1]
    assert len(s1) == 42, f"Expected 42 S01 episodes, got {len(s1)}"

def test_season01_no_gaps():
    from organize_classic_who import SERIALS
    nums = sorted(e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 1)
    assert nums == list(range(1, 43)), f"S01 gaps or dupes: {nums}"


# --- TASK 4: Seasons 02-03 ---

def test_season02_episode_count():
    from organize_classic_who import SERIALS
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 2]) == 39

def test_season03_episode_count():
    from organize_classic_who import SERIALS
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 3]) == 45


# --- TASK 5: Seasons 04-06 ---

def test_season04_episode_count():
    from organize_classic_who import SERIALS
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 4]) == 43

def test_season05_episode_count():
    from organize_classic_who import SERIALS
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 5]) == 40

def test_season06_episode_count():
    from organize_classic_who import SERIALS
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 6]) == 44


# --- TASK 6: Seasons 07-09 ---

def test_season07_episode_count():
    from organize_classic_who import SERIALS
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 7]) == 25

def test_season08_episode_count():
    from organize_classic_who import SERIALS
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 8]) == 25

def test_season09_episode_count():
    from organize_classic_who import SERIALS
    # 26 broadcast + 4 Day of the Daleks SE
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 9]) == 30


# --- TASK 7: Seasons 10-12 ---

def test_season10_episode_count():
    from organize_classic_who import SERIALS
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 10]) == 26

def test_season11_episode_count():
    from organize_classic_who import SERIALS
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 11]) == 26

def test_season12_episode_count():
    from organize_classic_who import SERIALS
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 12]) == 20


# --- TASK 8: Seasons 13-15 ---

def test_season13_episode_count():
    from organize_classic_who import SERIALS
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 13]) == 26

def test_season14_episode_count():
    from organize_classic_who import SERIALS
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 14]) == 26

def test_season15_episode_count():
    from organize_classic_who import SERIALS
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 15]) == 26


# --- TASK 9: Seasons 16-18 ---

def test_season16_episode_count():
    from organize_classic_who import SERIALS
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 16]) == 26

def test_season17_episode_count():
    from organize_classic_who import SERIALS
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 17]) == 20

def test_season18_episode_count():
    from organize_classic_who import SERIALS
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 18]) == 28


# --- TASK 10: Seasons 19-20 ---

def test_season19_episode_count():
    from organize_classic_who import SERIALS
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 19]) == 26

def test_season20_episode_count():
    from organize_classic_who import SERIALS
    # 22 broadcast + Five Doctors Transmission (S20E23) + Enlightenment SE (S20E24) + Five Doctors SE (S20E25)
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 20]) == 25


# --- TASK 11: Seasons 21-23 ---

def test_season21_episode_count():
    from organize_classic_who import SERIALS
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 21]) == 26

def test_season22_episode_count():
    from organize_classic_who import SERIALS
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 22]) == 13

def test_season23_episode_count():
    from organize_classic_who import SERIALS
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 23]) == 14


# --- TASK 12: Seasons 24-26 ---

def test_season24_episode_count():
    from organize_classic_who import SERIALS
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 24]) == 14

def test_season25_episode_count():
    from organize_classic_who import SERIALS
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 25]) == 14

def test_season26_episode_count():
    from organize_classic_who import SERIALS
    assert len([e for entry in SERIALS for (s,e,_,_) in entry["episodes"] if s == 26]) == 14
