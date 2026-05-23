from pathlib import Path
import os, shutil, logging, argparse

logging.basicConfig(level=logging.INFO, format="%(levelname)s  %(message)s")

SOURCE = Path("/media/madmaxlgndklr/media31/Shows/Ninja Sentai Kakuranger")
DEST   = Path("/media/madmaxlgndklr/media31/Shows/Ninja Sentai Kakuranger (1994)")

MANIFEST = [
    ("[G.U.I.S.] Ninja Sentai Kakuranger 01 (566184F9).mkv", DEST, 1, [1]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 02 (7B8D7673).mkv", DEST, 1, [2]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 03 (6D9960B0).mkv", DEST, 1, [3]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 04 (D543C3DE).mkv", DEST, 1, [4]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 05 (F297B6B7).mkv", DEST, 1, [5]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 06 (BCFC8320).mkv", DEST, 1, [6]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 07 (6F9ABB0F).mkv", DEST, 1, [7]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 08 (2B36B11A).mkv", DEST, 1, [8]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 09 (BB6C2B5A).mkv", DEST, 1, [9]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 10 (65582B68).mkv", DEST, 1, [10]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 11 (833485CA).mkv", DEST, 1, [11]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 12 (4D24312D).mkv", DEST, 1, [12]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 13 (2E1FCCE7).mkv", DEST, 1, [13]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 14 (19EA9F83).mkv", DEST, 1, [14]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 15 (0F39C6A5).mkv", DEST, 1, [15]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 16 (2BB48FFD).mkv", DEST, 1, [16]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 17 (E523AF2F).mkv", DEST, 1, [17]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 18 (BC103DB6).mkv", DEST, 1, [18]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 19 (C108F852).mkv", DEST, 1, [19]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 20 (5E6BA87F).mkv", DEST, 1, [20]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 21 (5C3A97EB).mkv", DEST, 1, [21]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 22 (1212F1EC).mkv", DEST, 1, [22]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 23 (EC259FA8).mkv", DEST, 1, [23]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 24 (E38CDB22).mkv", DEST, 1, [24]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 25 (F848977A).mkv", DEST, 1, [25]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 26 (E4198AE1).mkv", DEST, 1, [26]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 27 (53900C48).mkv", DEST, 1, [27]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 28 (936A8AF6).mkv", DEST, 1, [28]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 29 (79B762B4).mkv", DEST, 1, [29]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 30 (B45C4C1B).mkv", DEST, 1, [30]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 31 (209CE4B2).mkv", DEST, 1, [31]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 32 (2C9D7649).mkv", DEST, 1, [32]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 33 (E2088602).mkv", DEST, 1, [33]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 34 (7982FFC9).mkv", DEST, 1, [34]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 35 (49EA52F7).mkv", DEST, 1, [35]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 36 (13B7D1FC).mkv", DEST, 1, [36]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 37 (42E80356).mkv", DEST, 1, [37]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 38 (BF33DEF1).mkv", DEST, 1, [38]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 39 (0EDCC3A2).mkv", DEST, 1, [39]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 40 (05118A51).mkv", DEST, 1, [40]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 41 (39EABFC6).mkv", DEST, 1, [41]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 42 (8D4FD59F).mkv", DEST, 1, [42]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 43 (190E0013).mkv", DEST, 1, [43]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 44 (45BA6417).mkv", DEST, 1, [44]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 45 (C48EC43A).mkv", DEST, 1, [45]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 46 (AF8F6C94).mkv", DEST, 1, [46]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 47 (346CCA10).mkv", DEST, 1, [47]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 48 (AA1BE626).mkv", DEST, 1, [48]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 49 (12B76254).mkv", DEST, 1, [49]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 50 (6CCFDCE4).mkv", DEST, 1, [50]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 51 (A09807CD).mkv", DEST, 1, [51]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 52 (EF025C8E).mkv", DEST, 1, [52]),
    ("[G.U.I.S.] Ninja Sentai Kakuranger 53 (12EA695A).mkv", DEST, 1, [53]),
    # Movie → Season 0
    ("[G.U.I.S.] Ninja Sentai Kakuranger Movie (ADFA582E).mkv", DEST, 0, [1]),
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
