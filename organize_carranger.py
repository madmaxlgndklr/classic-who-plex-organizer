from pathlib import Path
import os, shutil, logging, argparse

logging.basicConfig(level=logging.INFO, format="%(levelname)s  %(message)s")

SOURCE = Path("/media/madmaxlgndklr/media31/Shows/Racing Squad Carranger")
DEST   = Path("/media/madmaxlgndklr/media31/Shows/Gekisou Sentai Carranger (1996)")

MANIFEST = [
    ("[HaroRangers] Gekisou Sentai Carranger - 01 [DVD][3A478ACD].mkv",       DEST, 1, [1]),
    ("[HaroRangers] Gekisou Sentai Carranger - 02 [DVD][78FB96F8].mkv",       DEST, 1, [2]),
    ("[HaroRangers] Gekisou Sentai Carranger - 03 [DVD][DBE209B0].mkv",       DEST, 1, [3]),
    ("[HaroRangers] Gekisou Sentai Carranger - 04 [DVD][FF704127].mkv",       DEST, 1, [4]),
    ("[HaroRangers] Gekisou Sentai Carranger - 05 [DVD][D2D58F00].mkv",       DEST, 1, [5]),
    ("[HaroRangers] Gekisou Sentai Carranger - 06 [DVD][0A6308AD].mkv",       DEST, 1, [6]),
    ("[HaroRangers] Gekisou Sentai Carranger - 07 [DVD][36C5BAB3].mkv",       DEST, 1, [7]),
    ("[HaroRangers] Gekisou Sentai Carranger - 08 [DVD][EC4280E7].mkv",       DEST, 1, [8]),
    ("[HaroRangers] Gekisou Sentai Carranger - 09 [DVD][C79ECC06].mkv",       DEST, 1, [9]),
    ("[HaroRangers] Gekisou Sentai Carranger - 10 [DVD][AA31BA33].mkv",       DEST, 1, [10]),
    ("[HaroRangers] Gekisou Sentai Carranger - 11 [DVD][89B2CA7A].mkv",       DEST, 1, [11]),
    ("[HaroRangers] Gekisou Sentai Carranger - 12 [DVD][FCC9D4B7].mkv",       DEST, 1, [12]),
    ("[HaroRangers] Gekisou Sentai Carranger - 13 [DVD][D87D5B31].mkv",       DEST, 1, [13]),
    ("[HaroRangers] Gekisou Sentai Carranger - 14 [DVD][49675A26].mkv",       DEST, 1, [14]),
    ("[HaroRangers] Gekisou Sentai Carranger - 15 [DVD][D256198C].mkv",       DEST, 1, [15]),
    ("[HaroRangers] Gekisou Sentai Carranger - 16 [DVD][E50CAE29].mkv",       DEST, 1, [16]),
    ("[HaroRangers] Gekisou Sentai Carranger - 17 [DVD][D2ABACF2].mkv",       DEST, 1, [17]),
    ("[HaroRangers] Gekisou Sentai Carranger - 18 [DVD][C24DB2BE].mkv",       DEST, 1, [18]),
    ("[HaroRangers] Gekisou Sentai Carranger - 19 [DVD][60575BF8].mkv",       DEST, 1, [19]),
    ("[HaroRangers] Gekisou Sentai Carranger - 20 [DVD][30B46B73].mkv",       DEST, 1, [20]),
    ("[HaroRangers] Gekisou Sentai Carranger - 21 [DVD][971E974C].mkv",       DEST, 1, [21]),
    ("[HaroRangers] Gekisou Sentai Carranger - 22 [DVD][4CC13E59].mkv",       DEST, 1, [22]),
    ("[HaroRangers] Gekisou Sentai Carranger - 23 [DVD][F0678C90].mkv",       DEST, 1, [23]),
    ("[HaroRangers] Gekisou Sentai Carranger - 24 [DVD][649B0C29].mkv",       DEST, 1, [24]),
    ("[HaroRangers] Gekisou Sentai Carranger - 25 [DVD][AA9041F9].mkv",       DEST, 1, [25]),
    ("[HaroRangers] Gekisou Sentai Carranger - 26 [DVD][F05D5F75].mkv",       DEST, 1, [26]),
    ("[HaroRangers] Gekisou Sentai Carranger - 27 [DVD][9D6640B0].mkv",       DEST, 1, [27]),
    ("[HaroRangers] Gekisou Sentai Carranger - 28 [DVD][3EB64E2F].mkv",       DEST, 1, [28]),
    ("[HaroRangers] Gekisou Sentai Carranger - 29 [DVD][03E053E3].mkv",       DEST, 1, [29]),
    ("[HaroRangers] Gekisou Sentai Carranger - 30 [DVD][A837B4E6].mkv",       DEST, 1, [30]),
    ("[HaroRangers] Gekisou Sentai Carranger - 31 [DVD][249f4926].mkv",       DEST, 1, [31]),
    ("[HaroRangers] Gekisou Sentai Carranger - 32 [DVD][1C1F14BA].mkv",       DEST, 1, [32]),
    ("[HaroRangers] Gekisou Sentai Carranger - 33 [DVD][2F5C0E2F].mkv",       DEST, 1, [33]),
    ("[HaroRangers] Gekisou Sentai Carranger - 34 [DVD][8DED11E6].mkv",       DEST, 1, [34]),
    ("[HaroRangers] Gekisou Sentai Carranger - 35 [DVD][D20360CC].mkv",       DEST, 1, [35]),
    ("[HaroRangers] Gekisou Sentai Carranger - 36 [DVD][521D428C].mkv",       DEST, 1, [36]),
    ("[HaroRangers] Gekisou Sentai Carranger - 37 [DVD][F5470A3D].mkv",       DEST, 1, [37]),
    ("[HaroRangers] Gekisou Sentai Carranger - 38 [DVD][6E8EF06B].mkv",       DEST, 1, [38]),
    ("[HaroRangers] Gekisou Sentai Carranger - 39 [DVD][88695805].mkv",       DEST, 1, [39]),
    ("[HaroRangers] Gekisou Sentai Carranger - 40 [DVD][0BAA0712].mkv",       DEST, 1, [40]),
    ("[HaroRangers] Gekisou Sentai Carranger - 41 [DVD][EDBFE1AD].mkv",       DEST, 1, [41]),
    ("[HaroRangers] Gekisou Sentai Carranger - 42 [DVD][85A46A5A].mkv",       DEST, 1, [42]),
    ("[HaroRangers] Gekisou Sentai Carranger - 43 [DVD][A6D37A93].mkv",       DEST, 1, [43]),
    ("[HaroRangers] Gekisou Sentai Carranger - 44 [DVD][9DD50758].mkv",       DEST, 1, [44]),
    ("[HaroRangers] Gekisou Sentai Carranger - 45 [DVD][43C130B4].mkv",       DEST, 1, [45]),
    ("[HaroRangers] Gekisou Sentai Carranger - 46 [DVD][B95FE016].mkv",       DEST, 1, [46]),
    ("[HaroRangers] Gekisou Sentai Carranger - 47 [DVD][AF93D8BB].mkv",       DEST, 1, [47]),
    ("[HaroRangers] Gekisou Sentai Carranger - 48 finale [DVD][C23F6BA0].mkv", DEST, 1, [48]),
]


def _show_name(dest_root): return dest_root.name
def _ep_tag(episodes): return "".join(f"E{e:02d}" for e in episodes)

def _dest_path(dest_root, season, episodes, ext=".mkv"):
    show = _show_name(dest_root)
    fname = f"{show} - S{season:02d}{_ep_tag(episodes)}{ext}"
    return dest_root / f"Season {season:02d}" / fname


def build_plan():
    moves = []
    for src_name, dest_root, season, episodes in MANIFEST:
        src = SOURCE / src_name
        dest = _dest_path(dest_root, season, episodes, Path(src_name).suffix)
        moves.append((src, dest))
    return moves


def execute(dry_run=False):
    moves = build_plan()
    errors, moved = 0, 0
    for src, dest in moves:
        if not src.exists():
            logging.warning("MISSING  %s", src.name)
            errors += 1
            continue
        if dry_run:
            logging.info("DRY-RUN  %s  →  %s", src.name, dest)
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            os.rename(src, dest)
        except OSError:
            shutil.move(str(src), str(dest))
        logging.info("MOVED    %s", dest.name)
        moved += 1
    logging.info("Done: %d moved, %d errors", moved, errors)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    execute(dry_run=args.dry_run)
