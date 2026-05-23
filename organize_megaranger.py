from pathlib import Path
import os, shutil, logging, argparse

logging.basicConfig(level=logging.INFO, format="%(levelname)s  %(message)s")

SOURCE = Path("/media/madmaxlgndklr/media31/Shows/Denji Sentai Megaranger")
DEST   = Path("/media/madmaxlgndklr/media31/Shows/Denji Sentai Megaranger (1997)")

MANIFEST = [
    ("[MFC] Denji Sentai Megaranger- 01v2 (48ACD4B9).mkv", DEST, 1, [1]),
    ("[MFC] Denji Sentai Megaranger- 02 (F0FFCAA0).mkv",   DEST, 1, [2]),
    ("[MFC] Denji Sentai Megaranger- 03 (A707B020).mkv",   DEST, 1, [3]),
    ("[MFC] Denji Sentai Megaranger- 04 (5F347B78).mkv",   DEST, 1, [4]),
    ("[MFC] Denji Sentai Megaranger- 05 (9E697897).mkv",   DEST, 1, [5]),
    ("[MFC] Denji Sentai Megaranger- 06v2 (C718FF6C).mkv", DEST, 1, [6]),
    ("[MFC] Denji Sentai Megaranger- 07 (0171CC0A).mkv",   DEST, 1, [7]),
    ("[MFC] Denji Sentai Megaranger- 08 (AD7B1FF9).mkv",   DEST, 1, [8]),
    ("[MFC] Denji Sentai Megaranger- 09 (E90E2D92).mkv",   DEST, 1, [9]),
    ("[MFC] Denji Sentai Megaranger- 10 (844F2155).mkv",   DEST, 1, [10]),
    ("[MFC] Denji Sentai Megaranger- 11 (122C2A61).mkv",   DEST, 1, [11]),
    ("[MFC] Denji Sentai Megaranger- 12 (6A57A536).mkv",   DEST, 1, [12]),
    ("[MFC] Denji Sentai Megaranger- 13 (B8CAF2F5).mkv",   DEST, 1, [13]),
    ("[MFC] Denji Sentai Megaranger- 14 (86242A05).mkv",   DEST, 1, [14]),
    ("[MFC] Denji Sentai Megaranger- 15 (BE7A1086).mkv",   DEST, 1, [15]),
    ("[MFC] Denji Sentai Megaranger- 16 (ED60C8E9).mkv",   DEST, 1, [16]),
    ("[MFC] Denji Sentai Megaranger- 17 (1EBB50EC).mkv",   DEST, 1, [17]),
    ("[MFC] Denji Sentai Megaranger- 18 (110AEC37).mkv",   DEST, 1, [18]),
    ("[MFC] Denji Sentai Megaranger- 19 (667DAE07).mkv",   DEST, 1, [19]),
    ("[MFC] Denji Sentai Megaranger- 20 (CA38EF37).mkv",   DEST, 1, [20]),
    ("[MFC] Denji Sentai Megaranger- 21 (C7BD254C).mkv",   DEST, 1, [21]),
    ("[MFC] Denji Sentai Megaranger- 22 (9CDC11E0).mkv",   DEST, 1, [22]),
    ("[MFC] Denji Sentai Megaranger- 23 (F277E94F).mkv",   DEST, 1, [23]),
    ("[MFC] Denji Sentai Megaranger- 24 (3BC0A6AF).mkv",   DEST, 1, [24]),
    ("[MFC] Denji Sentai Megaranger- 25 (2FFD301E).mkv",   DEST, 1, [25]),
    ("[MFC] Denji Sentai Megaranger- 26 (D24C8208).mkv",   DEST, 1, [26]),
    ("[MFC] Denji Sentai Megaranger- 27 (F8D84537).mkv",   DEST, 1, [27]),
    ("[MFC] Denji Sentai Megaranger- 28 (362B491B).mkv",   DEST, 1, [28]),
    ("[MFC] Denji Sentai Megaranger- 29 (7A31E382).mkv",   DEST, 1, [29]),
    ("[MFC] Denji Sentai Megaranger- 30 (6021F7A4).mkv",   DEST, 1, [30]),
    ("[MFC] Denji Sentai Megaranger- 31 (FC720613).mkv",   DEST, 1, [31]),
    ("[MFC] Denji Sentai Megaranger- 32 (EB050776).mkv",   DEST, 1, [32]),
    ("[MFC] Denji Sentai Megaranger- 33 (4886E375).mkv",   DEST, 1, [33]),
    ("[MFC] Denji Sentai Megaranger- 34 (94C6AE8F).mkv",   DEST, 1, [34]),
    ("[MFC] Denji Sentai Megaranger- 35 (2F903963).mkv",   DEST, 1, [35]),
    ("[MFC] Denji Sentai Megaranger- 36 (222E21CE).mkv",   DEST, 1, [36]),
    ("[MFC] Denji Sentai Megaranger- 37 (44FFFAFE).mkv",   DEST, 1, [37]),
    ("[MFC] Denji Sentai Megaranger- 38 (1D7E7195).mkv",   DEST, 1, [38]),
    ("[MFC] Denji Sentai Megaranger- 39 (BFA17285).mkv",   DEST, 1, [39]),
    ("[MFC] Denji Sentai Megaranger- 40 (E5D3DFD1).mkv",   DEST, 1, [40]),
    ("[MFC] Denji Sentai Megaranger- 41 (50AE8484).mkv",   DEST, 1, [41]),
    ("[MFC] Denji Sentai Megaranger- 42 (A682B7CE).mkv",   DEST, 1, [42]),
    ("[MFC] Denji Sentai Megaranger- 43 (658BE333).mkv",   DEST, 1, [43]),
    ("[MFC] Denji Sentai Megaranger- 44 (3721B262).mkv",   DEST, 1, [44]),
    ("[MFC] Denji Sentai Megaranger- 45 (A18C9A39).mkv",   DEST, 1, [45]),
    ("[MFC] Denji Sentai Megaranger- 46 (32E6EB58).mkv",   DEST, 1, [46]),
    ("[MFC] Denji Sentai Megaranger- 47 (2E202AE6).mkv",   DEST, 1, [47]),
    ("[MFC] Denji Sentai Megaranger- 48 (611A6A10).mkv",   DEST, 1, [48]),
    ("[MFC] Denji Sentai Megaranger- 49 (81A85C61).mkv",   DEST, 1, [49]),
    ("[MFC] Denji Sentai Megaranger- 50 (D2614891).mkv",   DEST, 1, [50]),
    ("[MFC] Denji Sentai Megaranger- 51 (39BFC846).mkv",   DEST, 1, [51]),
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
