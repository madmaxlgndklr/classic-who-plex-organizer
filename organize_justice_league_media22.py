from pathlib import Path
import os, shutil, argparse, logging

SOURCE   = Path("/media/madmaxlgndklr/media22/shows/Justice League (Unlimited)")
JL_DEST  = Path("/media/madmaxlgndklr/media22/shows/Justice League (2001)")
JLU_DEST = Path("/media/madmaxlgndklr/media22/shows/Justice League Unlimited")

# media22 copy of the JL collection. Mostly mirrors media31 but 12 files
# use a different naming scheme (Justice League S01EXX.avi) — those are
# handled directly below. Secret Origins is S01E01 only (single part).
MANIFEST = [
    # ── Justice League Season 1 ───────────────────────────────────────────────
    ("Justice League S01E01.avi",                          JL_DEST, 1, [1],     "Secret Origins"),
    ("JL #4 In Blackest Night 1.avi",                      JL_DEST, 1, [4],     "In Blackest Night, Part I"),
    ("JL #5 In Blackest Night 2.avi",                      JL_DEST, 1, [5],     "In Blackest Night, Part II"),
    ("JL #6 The Enemy Below 1.avi",                        JL_DEST, 1, [6],     "The Enemy Below, Part I"),
    ("JL #7 The Enemy Below 2.avi",                        JL_DEST, 1, [7],     "The Enemy Below, Part II"),
    ("JL #8 Paradise Lost 1.avi",                          JL_DEST, 1, [10],    "Paradise Lost, Part I"),
    ("JL #9 Paradise Lost 2.avi",                          JL_DEST, 1, [11],    "Paradise Lost, Part II"),
    ("JL #10 War World 1.avi",                             JL_DEST, 1, [12],    "War World, Part I"),
    ("JL #11 War World 2.avi",                             JL_DEST, 1, [13],    "War World, Part II"),
    ("JL #12 The Brave and the Bold 1.avi",                JL_DEST, 1, [14],    "The Brave and the Bold, Part I"),
    ("JL #13 The Brave and the Bold 2.avi",                JL_DEST, 1, [15],    "The Brave and the Bold, Part II"),
    ("JL #14 Fury 1.avi",                                  JL_DEST, 1, [16],    "Fury, Part I"),
    ("JL #15 Fury 2.avi",                                  JL_DEST, 1, [17],    "Fury, Part II"),
    ("JL #16 Legends 1.avi",                               JL_DEST, 1, [18],    "Legends, Part I"),
    ("JL #17 Legends 2.avi",                               JL_DEST, 1, [19],    "Legends, Part II"),
    ("JL #18 Injustice for All 1.avi",                     JL_DEST, 1, [8],     "Injustice for All, Part I"),
    ("JL #19 Injustice For All 2.avi",                     JL_DEST, 1, [9],     "Injustice for All, Part II"),
    ("JL #20 A Knight of Shadows 1.avi",                   JL_DEST, 1, [20],    "A Knight of Shadows, Part I"),
    ("JL #21 A Knight of Shadows 2.avi",                   JL_DEST, 1, [21],    "A Knight of Shadows, Part II"),
    ("JL #22 Metamorphisis 1.avi",                         JL_DEST, 1, [22],    "Metamorphosis, Part I"),
    ("JL #23 Metamorphisis 2.avi",                         JL_DEST, 1, [23],    "Metamorphosis, Part II"),
    ("JL #24 The Savage Time 1.avi",                       JL_DEST, 1, [24],    "The Savage Time, Part I"),
    ("JL #25 The Savage Time 2.avi",                       JL_DEST, 1, [25],    "The Savage Time, Part II"),
    ("JL #26 The Savage Time 3.avi",                       JL_DEST, 1, [26],    "The Savage Time, Part III"),
    # ── Justice League Season 2 ───────────────────────────────────────────────
    ("JL #27 - 28 Twilight of the Gods.avi",               JL_DEST, 2, [1,2],   "Twilight of the Gods"),
    ("JL #29 - 30 Tabula Rasa.avi",                        JL_DEST, 2, [3,4],   "Tabula Rasa"),
    ("JL #31 - 32 Only a Dream.avi",                       JL_DEST, 2, [5,6],   "Only a Dream"),
    ("JL #33 - 34 Maid of Honor.avi",                      JL_DEST, 2, [7,8],   "Maid of Honor"),
    ("JL #35 - 36 Hearts and Minds.avi",                   JL_DEST, 2, [9,10],  "Hearts and Minds"),
    ("JL #37 - 38 A Better World.avi",                     JL_DEST, 2, [11,12], "A Better World"),
    ("JL #39 - 40 Eclipsed.avi",                           JL_DEST, 2, [13,14], "Eclipsed"),
    ("JL #41- 42 The Terror Beyond.avi",                   JL_DEST, 2, [15,16], "The Terror Beyond"),
    ("JL #43 - 44 Secret Society.avi",                     JL_DEST, 2, [17,18], "Secret Society"),
    ("JL #45 - 46 Hereafter.avi",                          JL_DEST, 2, [19,20], "Hereafter"),
    ("JL #47 - 48 Wildcards.avi",                          JL_DEST, 2, [21,22], "Wildcards"),
    ("JL #49 Comfort and Joy.avi",                         JL_DEST, 2, [23],    "Comfort and Joy"),
    ("JL #50 Starcrossed 1.avi",                           JL_DEST, 2, [24],    "Starcrossed, Part I"),
    ("JL #51 Starcrossed 2.avi",                           JL_DEST, 2, [25],    "Starcrossed, Part II"),
    ("JL #52 Starcrossed 3.avi",                           JL_DEST, 2, [26],    "Starcrossed, Part III"),
    # ── Justice League Unlimited Season 1 ────────────────────────────────────
    ("JL #53 Initiation (U).avi",                          JLU_DEST, 1, [1],  "Initiation"),
    ("JL #54 For the Man Who Has Everything (U).avi",      JLU_DEST, 1, [2],  "For the Man Who Has Everything"),
    ("JL #55 Kid Stuff (U).avi",                           JLU_DEST, 1, [3],  "Kid Stuff"),
    ("JL #56 Hawk and Dove (U).avi",                       JLU_DEST, 1, [4],  "Hawk and Dove"),
    ("JL #57 This LIttle Piggy (U).avi",                   JLU_DEST, 1, [5],  "This Little Piggy"),
    ("JL #58 Fearful Symmetry (U).avi",                    JLU_DEST, 1, [6],  "Fearful Symmetry"),
    ("JL #59 The Greatest Story Never Told (U).avi",       JLU_DEST, 1, [7],  "The Greatest Story Never Told"),
    ("JL #60 The Return (U).avi",                          JLU_DEST, 1, [8],  "The Return"),
    ("JL #61 Ultimatum (U).avi",                           JLU_DEST, 1, [9],  "Ultimatum"),
    ("JL #62 Dark Heart (U).avi",                          JLU_DEST, 1, [10], "Dark Heart"),
    ("JL #63 Wake the Dead (U).avi",                       JLU_DEST, 1, [11], "Wake the Dead"),
    ("Justice League S01E64.avi",                          JLU_DEST, 1, [12], "The Once and Future Thing: Weird Western Tales"),
    ("Justice League S01E65.avi",                          JLU_DEST, 1, [13], "The Once and Future Thing: Time, Warped"),
    # ── Justice League Unlimited Season 2 ────────────────────────────────────
    ("JL #66 The Cat and the Canary (U).avi",              JLU_DEST, 2, [1],  "The Cat and the Canary"),
    ("JL #67 The Ties That Bind (U).avi",                  JLU_DEST, 2, [2],  "The Ties That Bind"),
    ("JL #68 The Doomsday Sanction (U).avi",               JLU_DEST, 2, [3],  "The Doomsday Sanction"),
    ("JL #69 Task Force X (U).avi",                        JLU_DEST, 2, [4],  "Task Force X"),
    ("JL #70 The Balance (U).avi",                         JLU_DEST, 2, [5],  "The Balance"),
    ("JL #71 Double Date (U).avi",                         JLU_DEST, 2, [6],  "Double Date"),
    ("JL #72 Clash (U).avi",                               JLU_DEST, 2, [7],  "Clash"),
    ("JL #73 Hunter's Moon (U).avi",                       JLU_DEST, 2, [8],  "Hunter's Moon"),
    ("JL #74 Question Authority (U).avi",                  JLU_DEST, 2, [9],  "Question Authority"),
    ("JL #75 Flashpoint (U).avi",                          JLU_DEST, 2, [10], "Flashpoint"),
    ("JL #76 Panic In The Sky (U).avi",                    JLU_DEST, 2, [11], "Panic in the Sky"),
    ("JL #77 Divided We Fall (U).avi",                     JLU_DEST, 2, [12], "Divided We Fall"),
    ("Justice League - S01E78 - Epilogue.avi",             JLU_DEST, 2, [13], "Epilogue"),
    # ── Justice League Unlimited Season 3 ────────────────────────────────────
    ("Justice League S01E79.avi",                          JLU_DEST, 3, [1],  "I Am Legion"),
    ("JL # 80 Shadow of the Hawk (U).avi",                 JLU_DEST, 3, [2],  "Shadow of the Hawk"),
    ("JL # 81 Chaos at the Earth's Core (U).avi",          JLU_DEST, 3, [3],  "Chaos at the Earth's Core"),
    ("JL # 82 To Another Shore (U).avi",                   JLU_DEST, 3, [4],  "To Another Shore"),
    ("JL # 83 Flash and Substance (U).avi",                JLU_DEST, 3, [5],  "Flash and Substance"),
    ("JL # 84 Dead Reckoning (U).avi",                     JLU_DEST, 3, [6],  "Dead Reckoning"),
    ("Justice League S01E85.avi",                          JLU_DEST, 3, [7],  "Patriot Act"),
    ("Justice League S01E86.avi",                          JLU_DEST, 3, [8],  "The Great Brain Robbery"),
    ("Justice League S01E87.avi",                          JLU_DEST, 3, [9],  "Grudge Match"),
    ("Justice League S01E88.avi",                          JLU_DEST, 3, [10], "Far From Home"),
    ("Justice League S01E89.avi",                          JLU_DEST, 3, [11], "Ancient History"),
    ("Justice League S01E90.avi",                          JLU_DEST, 3, [12], "Alive!"),
    ("Justice League S01E91.avi",                          JLU_DEST, 3, [13], "Destroyer"),
]


def _show_name(dest_root: Path) -> str:
    return dest_root.name


def _ep_tag(episodes: list) -> str:
    return "".join(f"E{e:02d}" for e in episodes)


def _dest_path(dest_root: Path, season: int, episodes: list, title: str, ext: str = ".avi") -> Path:
    show = _show_name(dest_root)
    fname = f"{show} - S{season:02d}{_ep_tag(episodes)} - {title}{ext}"
    return dest_root / f"Season {season:02d}" / fname


def build_plan() -> list:
    moves = []
    for src_name, dest_root, season, episodes, title in MANIFEST:
        src = SOURCE / src_name
        dest = _dest_path(dest_root, season, episodes, title, Path(src_name).suffix)
        moves.append((src, dest))
    return moves


def execute_plan(moves: list, dry_run: bool = True) -> tuple:
    moved = skipped = errors = 0
    for src, dest in moves:
        if not src.exists():
            logging.warning(f"WARN  source missing: {src.name}")
            errors += 1
            continue
        if dest.exists():
            logging.info(f"SKIP  {dest.name}")
            skipped += 1
            continue
        if dry_run:
            logging.info(f"DRY   {src.name}\n   -> {dest}")
            moved += 1
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            try:
                os.rename(src, dest)
            except OSError:
                shutil.move(str(src), str(dest))
            logging.info(f"MOVE  {src.name}\n   -> {dest}")
            moved += 1
    return moved, skipped, errors


def main():
    parser = argparse.ArgumentParser(description="Reorganize Justice League (media22) files for Plex")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true")
    group.add_argument("--execute", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("organize_justice_league_media22.log"),
        ],
    )

    moves = build_plan()
    logging.info(f"\nPlan: {len(moves)} file operations")
    moved, skipped, errors = execute_plan(moves, dry_run=not args.execute)
    logging.info(f"\nSummary: moved={moved}  skipped={skipped}  errors={errors}")


if __name__ == "__main__":
    main()
