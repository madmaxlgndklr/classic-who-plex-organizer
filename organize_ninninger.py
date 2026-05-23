from pathlib import Path
import os, shutil, logging, argparse

logging.basicConfig(level=logging.INFO, format="%(levelname)s  %(message)s")

SOURCE = Path("/media/madmaxlgndklr/media31/Shows/Shuriken Sentai Ninninger")
DEST   = Path("/media/madmaxlgndklr/media31/Shows/Shuriken Sentai Ninninger (2015)")

MANIFEST = [
    ("[Over-Time] Shuriken Sentai Ninninger - 01 [8874C8AC].mkv", DEST, 1, [1]),
    ("[Over-Time] Shuriken Sentai Ninninger - 02 [B96BD95B].mkv", DEST, 1, [2]),
    ("[Over-Time] Shuriken Sentai Ninninger - 03 [1A175F1C].mkv", DEST, 1, [3]),
    ("[Over-Time] Shuriken Sentai Ninninger - 04 [690DB7DB].mkv", DEST, 1, [4]),
    ("[Over-Time] Shuriken Sentai Ninninger - 05 [9AEBA6E8].mkv", DEST, 1, [5]),
    ("[Over-Time] Shuriken Sentai Ninninger - 06 [0E32983B].mkv", DEST, 1, [6]),
    ("[Over-Time] Shuriken Sentai Ninninger - 07 [8D0BB61F].mkv", DEST, 1, [7]),
    ("[Over-Time] Shuriken Sentai Ninninger - 08 [9199E2FF].mkv", DEST, 1, [8]),
    ("[Over-Time] Shuriken Sentai Ninninger - 09 [0670C7A3].mkv", DEST, 1, [9]),
    ("[Over-Time] Shuriken Sentai Ninninger - 10 [B3F8FCCF].mkv", DEST, 1, [10]),
    ("[Over-Time] Shuriken Sentai Ninninger - 11 [C45A03F9].mkv", DEST, 1, [11]),
    ("[Over-Time] Shuriken Sentai Ninninger - 12 [D55D2D51].mkv", DEST, 1, [12]),
    ("[Over-Time] Shuriken Sentai Ninninger - 13 [2D79392F].mkv", DEST, 1, [13]),
    ("[Over-Time] Shuriken Sentai Ninninger - 14 [2EBD0806].mkv", DEST, 1, [14]),
    ("[Over-Time] Shuriken Sentai Ninninger - 15 [38C61906].mkv", DEST, 1, [15]),
    ("[Over-Time] Shuriken Sentai Ninninger - 16 [02801371].mkv", DEST, 1, [16]),
    ("[Over-Time] Shuriken Sentai Ninninger - 17 [590216B4].mkv", DEST, 1, [17]),
    ("[Over-Time] Shuriken Sentai Ninninger - 18 [16B99379].mkv", DEST, 1, [18]),
    ("[Over-Time] Shuriken Sentai Ninninger - 19 [EA034178].mkv", DEST, 1, [19]),
    ("[Over-Time] Shuriken Sentai Ninninger - 20 [7FBB5877].mkv", DEST, 1, [20]),
    ("[Over-Time] Shuriken Sentai Ninninger - 21 [818CC9EB].mkv", DEST, 1, [21]),
    ("[Over-Time] Shuriken Sentai Ninninger - 22 [D4C83ACB].mkv", DEST, 1, [22]),
    ("[Over-Time] Shuriken Sentai Ninninger - 23 [50F1A43B].mkv", DEST, 1, [23]),
    ("[Over-Time] Shuriken Sentai Ninninger - 24 [FFAAA862].mkv", DEST, 1, [24]),
    ("[Over-Time] Shuriken Sentai Ninninger - 25 [3BE40903].mkv", DEST, 1, [25]),
    ("[Over-Time] Shuriken Sentai Ninninger - 26 [0EF3DB33].mkv", DEST, 1, [26]),
    ("[Over-Time] Shuriken Sentai Ninninger - 27 [9754F350].mkv", DEST, 1, [27]),
    ("[Over-Time] Shuriken Sentai Ninninger - 28 [4C238FEC].mkv", DEST, 1, [28]),
    ("[Over-Time] Shuriken Sentai Ninninger - 29 [4FF8926C].mkv", DEST, 1, [29]),
    ("[Over-Time] Shuriken Sentai Ninninger - 30 [B7FFFFF7].mkv", DEST, 1, [30]),
    ("[Over-Time] Shuriken Sentai Ninninger - 31 [CE6DE03D].mkv", DEST, 1, [31]),
    ("[Over-Time] Shuriken Sentai Ninninger - 32 [E2249A80].mkv", DEST, 1, [32]),
    ("[Over-Time] Shuriken Sentai Ninninger - 33 [EC20D605].mkv", DEST, 1, [33]),
    ("[Over-Time] Shuriken Sentai Ninninger - 34 [A13CAD12].mkv", DEST, 1, [34]),
    ("[Over-Time] Shuriken Sentai Ninninger - 35 [B2C4E7F7].mkv", DEST, 1, [35]),
    ("[Over-Time] Shuriken Sentai Ninninger - 36 [B223E5E6].mkv", DEST, 1, [36]),
    ("[Over-Time] Shuriken Sentai Ninninger - 37 [6E13A163].mkv", DEST, 1, [37]),
    ("[Over-Time] Shuriken Sentai Ninninger - 38 [A783C525].mkv", DEST, 1, [38]),
    ("[Over-Time] Shuriken Sentai Ninninger - 39 [A502F7C7].mkv", DEST, 1, [39]),
    ("[Over-Time] Shuriken Sentai Ninninger - 40 [418602D1].mkv", DEST, 1, [40]),
    ("[Over-Time] Shuriken Sentai Ninninger - 41 [B1372E3E].mkv", DEST, 1, [41]),
    ("[Over-Time] Shuriken Sentai Ninninger - 42 [BAB90A1B].mkv", DEST, 1, [42]),
    ("[Over-Time] Shuriken Sentai Ninninger - 43 [07614F5A].mkv", DEST, 1, [43]),
    ("[Over-Time] Shuriken Sentai Ninninger - 44 [DF22AC6B].mkv", DEST, 1, [44]),
    ("[Over-Time] Shuriken Sentai Ninninger - 45 [DE28DD88].mkv", DEST, 1, [45]),
    ("[Over-Time] Shuriken Sentai Ninninger - 46 [72622946].mkv", DEST, 1, [46]),
    ("[Over-Time] Shuriken Sentai Ninninger - 47 [36594BEA].mkv", DEST, 1, [47]),
    # VS special → Season 0
    ("[Over-Time] Shuriken Sentai Ninninger VS Kamen Rider Drive [17B2CA38].mkv", DEST, 0, [1]),
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
