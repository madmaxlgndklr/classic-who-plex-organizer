from pathlib import Path
import os, shutil, logging, argparse

logging.basicConfig(level=logging.INFO, format="%(levelname)s  %(message)s")

SOURCE = Path("/media/madmaxlgndklr/media31/Shows/Bioman")
DEST   = Path("/media/madmaxlgndklr/media31/Shows/Choudenshi Bioman (1984)")

MANIFEST = [
    ("[G.U.I.S.] Choudenshi Bioman 01 (7FA82281).mkv",  DEST, 1, [1]),
    ("[G.U.I.S.] Choudenshi Bioman 02 (9E9FB396).mkv",  DEST, 1, [2]),
    ("[G.U.I.S.] Choudenshi Bioman 03 (A808549F).mkv",  DEST, 1, [3]),
    ("[G.U.I.S.] Choudenshi Bioman 04 (08B44F14).mkv",  DEST, 1, [4]),
    ("[G.U.I.S.] Choudenshi Bioman 05 (ABA2E7B6).mkv",  DEST, 1, [5]),
    ("[G.U.I.S.] Choudenshi Bioman 06 (8752B49C).mkv",  DEST, 1, [6]),
    ("[G.U.I.S.] Choudenshi Bioman 07 (1A5A3457).mkv",  DEST, 1, [7]),
    ("[G.U.I.S.] Choudenshi Bioman 08 (60FCFC86).mkv",  DEST, 1, [8]),
    ("[G.U.I.S.] Choudenshi Bioman 09 (B8F9539F).mkv",  DEST, 1, [9]),
    ("[G.U.I.S.] Choudenshi Bioman 10 (E83A6B43).mkv",  DEST, 1, [10]),
    ("[G.U.I.S.] Choudenshi Bioman 11 (1DCBD571).mkv",  DEST, 1, [11]),
    ("[G.U.I.S.] Choudenshi Bioman 12 (7752422F).mkv",  DEST, 1, [12]),
    ("[G.U.I.S.] Choudenshi Bioman 13 (652E8D4F).mkv",  DEST, 1, [13]),
    ("[G.U.I.S.] Choudenshi Bioman 14 (184C26CD).mkv",  DEST, 1, [14]),
    ("[G.U.I.S.] Choudenshi Bioman 15 (308BBF7A).mkv",  DEST, 1, [15]),
    ("[G.U.I.S.] Choudenshi Bioman 16 (D5CA2183).mkv",  DEST, 1, [16]),
    ("[G.U.I.S.] Choudenshi Bioman 17 (E9B3CF33).mkv",  DEST, 1, [17]),
    ("[G.U.I.S.] Choudenshi Bioman 18 (82256E1E).mkv",  DEST, 1, [18]),
    ("[G.U.I.S.] Choudenshi Bioman 19 (143A3EC5).mkv",  DEST, 1, [19]),
    ("[G.U.I.S.] Choudenshi Bioman 20 (E4EB359B).mkv",  DEST, 1, [20]),
    ("[G.U.I.S.] Choudenshi Bioman 21 (8BB028CD).mkv",  DEST, 1, [21]),
    ("[G.U.I.S.] Choudenshi Bioman 22 (25260506).mp4",  DEST, 1, [22]),
    ("[G.U.I.S.] Choudenshi Bioman 23 (F02E151A).mkv",  DEST, 1, [23]),
    ("[G.U.I.S.] Choudenshi Bioman 24 (E2AF4273).mkv",  DEST, 1, [24]),
    ("[G.U.I.S.] Choudenshi Bioman 25 (CD5D1AE6).mkv",  DEST, 1, [25]),
    ("[G.U.I.S.] Choudenshi Bioman 26 (C546DBC1).mkv",  DEST, 1, [26]),
    ("[G.U.I.S.] Choudenshi Bioman 27 (78835CF4).mkv",  DEST, 1, [27]),
    ("[G.U.I.S.] Choudenshi Bioman 28 (7144B50B).mkv",  DEST, 1, [28]),
    ("[G.U.I.S.] Choudenshi Bioman 29 (F4B24042).mkv",  DEST, 1, [29]),
    ("[G.U.I.S.] Choudenshi Bioman 30 (D359001E).mkv",  DEST, 1, [30]),
    ("[G.U.I.S.] Choudenshi Bioman 31 (ABC3160C).mkv",  DEST, 1, [31]),
    ("[G.U.I.S.] Choudenshi Bioman 32 (D1217EBE).mkv",  DEST, 1, [32]),
    ("[G.U.I.S.] Choudenshi Bioman 33 (25B63689).mkv",  DEST, 1, [33]),
    ("[G.U.I.S.] Choudenshi Bioman 34 (1DA81395).mkv",  DEST, 1, [34]),
    ("[G.U.I.S.] Choudenshi Bioman 35 (30713B4F).mkv",  DEST, 1, [35]),
    ("[G.U.I.S.] Choudenshi Bioman 36 (E525B3EE).mkv",  DEST, 1, [36]),
    ("[G.U.I.S.] Choudenshi Bioman 37 (B1B442E5).mkv",  DEST, 1, [37]),
    ("[G.U.I.S.] Choudenshi Bioman 38 (9FEC790A).mkv",  DEST, 1, [38]),
    ("[G.U.I.S.] Choudenshi Bioman 39 (FBF1D68F).mkv",  DEST, 1, [39]),
    ("[G.U.I.S.] Choudenshi Bioman 40 (8CFF6BAE).mkv",  DEST, 1, [40]),
    ("[G.U.I.S.] Choudenshi Bioman 41 (654F1E83).mkv",  DEST, 1, [41]),
    ("[G.U.I.S.] Choudenshi Bioman 42 (166A90EB).mkv",  DEST, 1, [42]),
    ("[G.U.I.S.] Choudenshi Bioman 43 (CA9B17DA).mkv",  DEST, 1, [43]),
    ("[G.U.I.S.] Choudenshi Bioman 44 (9F684D7D).mkv",  DEST, 1, [44]),
    ("[G.U.I.S.] Choudenshi Bioman 45 (C6BBFEC7).mkv",  DEST, 1, [45]),
    ("[G.U.I.S.] Choudenshi Bioman 46 (67F43954).mkv",  DEST, 1, [46]),
    ("[G.U.I.S.] Choudenshi Bioman 47 (A8680CC0).mkv",  DEST, 1, [47]),
    ("[G.U.I.S.] Choudenshi Bioman 48 (0B42F9F5).mkv",  DEST, 1, [48]),
    ("[G.U.I.S.] Choudenshi Bioman 49 (3474C71E).mkv",  DEST, 1, [49]),
    ("[G.U.I.S.] Choudenshi Bioman 50 (9C35C8DA).mkv",  DEST, 1, [50]),
    ("[G.U.I.S.] Choudenshi Bioman 51 (E8E7FB32).mkv",  DEST, 1, [51]),
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
