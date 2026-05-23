from pathlib import Path
import os, shutil, logging, argparse

logging.basicConfig(level=logging.INFO, format="%(levelname)s  %(message)s")

# Source files use "Kyouryuu" (alternate romanization); TheTVDB name is "Kyoryu Sentai Zyuranger".
SOURCE = Path("/media/madmaxlgndklr/media31/Shows/Kyoryu Sentai Zyuranger")
DEST   = Path("/media/madmaxlgndklr/media31/Shows/Kyoryu Sentai Zyuranger (1992)")

MANIFEST = [
    ("[GUIS] Kyouryuu Sentai Zyuranger- 01 (018A4A15).mkv", DEST, 1, [1]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 02 (D51007B2).mkv", DEST, 1, [2]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 03 (4E0F071E).mkv", DEST, 1, [3]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 04 (5936B678).mkv", DEST, 1, [4]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 05 (4ED5CF84).mkv", DEST, 1, [5]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 06 (88EF709A).mkv", DEST, 1, [6]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 07 (909DF003).mkv", DEST, 1, [7]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 08 (CF83DB02).mkv", DEST, 1, [8]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 09 (B33F36F3).mkv", DEST, 1, [9]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 10 (B4F71F5E).mkv", DEST, 1, [10]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 11 (E59EB6D3).mkv", DEST, 1, [11]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 12 (39F02B2E).mkv", DEST, 1, [12]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 13 (F81DAB74).mkv", DEST, 1, [13]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 14 (52FF5EA7).mkv", DEST, 1, [14]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 15 (CD1BD5C8).mkv", DEST, 1, [15]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 16 (25DC4879).mkv", DEST, 1, [16]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 17 (FAB6EC93).mkv", DEST, 1, [17]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 18 (42489FDA).mkv", DEST, 1, [18]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 19 (81725DD6).mkv", DEST, 1, [19]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 20 (31DC8A32).mkv", DEST, 1, [20]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 21 (F59F2CB1).mkv", DEST, 1, [21]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 22 (2C3489E4).mkv", DEST, 1, [22]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 23 (54CA58B3).mkv", DEST, 1, [23]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 24 (178AF255).mkv", DEST, 1, [24]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 25 (34F00F10).mkv", DEST, 1, [25]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 26 (21B2E7F1).mkv", DEST, 1, [26]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 27 (28C0EFE7).mkv", DEST, 1, [27]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 28 (D59B49A2).mkv", DEST, 1, [28]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 29 (0B30F7BB).mkv", DEST, 1, [29]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 30 (302336E6).mkv", DEST, 1, [30]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 31v2 (F3411A94).mkv", DEST, 1, [31]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 32 (B2A78498).mkv", DEST, 1, [32]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 33 (08574A82).mkv", DEST, 1, [33]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 34 (ED8F3D5C).mkv", DEST, 1, [34]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 35 (C88CC408).mkv", DEST, 1, [35]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 36 (126DB532).mkv", DEST, 1, [36]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 37 (7F369CFB).mkv", DEST, 1, [37]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 38 (96ECC734).mkv", DEST, 1, [38]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 39 (19378FF1).mkv", DEST, 1, [39]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 40 (E1A820F0).mkv", DEST, 1, [40]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 41 (E3039D31).mkv", DEST, 1, [41]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 42 (FE652329).mkv", DEST, 1, [42]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 43 (C0EA8C91).mkv", DEST, 1, [43]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 44 (0E10FE94).mkv", DEST, 1, [44]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 45 (5C73DD36).mkv", DEST, 1, [45]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 46 (C73D57D3).mkv", DEST, 1, [46]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 47 (A9A9B6A5).mkv", DEST, 1, [47]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 48 (B8D02997).mkv", DEST, 1, [48]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 49 (18C2CC45).mkv", DEST, 1, [49]),
    ("[GUIS] Kyouryuu Sentai Zyuranger- 50 (EC816382).mkv", DEST, 1, [50]),
    # Specials → Season 0
    ("[GUIS] Kyouryuu Sentai Zyuranger Dino Video (A4947257).mkv",            DEST, 0, [1]),
    ("[GUIS] Kyouryuu Sentai Zyuranger Preview (662FA17D).mkv",               DEST, 0, [2]),
    ("[GUIS] Reiko Chiba and Machiko Soga Interview (E70BD30E).mkv",          DEST, 0, [3]),
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
