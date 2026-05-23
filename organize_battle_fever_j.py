from pathlib import Path
import os, shutil, logging, argparse

logging.basicConfig(level=logging.INFO, format="%(levelname)s  %(message)s")

SOURCE = Path("/media/madmaxlgndklr/media31/Shows/Battle Fever J")
DEST   = Path("/media/madmaxlgndklr/media31/Shows/Battle Fever J (1979)")

MANIFEST = [
    # (source_filename, dest_root, season, [episode_numbers])
    # Season 0 — pre-series special
    ("[Bunny_Hat_Raw]Battle_Fever_J_00_(02E23F8A).mkv", DEST, 0, [0]),
    # Season 1 — episodes 1–52
    ("[Bunny_Hat_Raw]Battle_Fever_J_01_(325F11EF).mkv", DEST, 1, [1]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_02_(CA7187AE).mkv", DEST, 1, [2]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_03_(22FD32BD).mkv", DEST, 1, [3]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_04_(415A842F).mkv", DEST, 1, [4]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_05_(D91B06D9).mkv", DEST, 1, [5]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_06_(E1828367).mkv", DEST, 1, [6]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_07_(A59EA00F).mkv", DEST, 1, [7]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_08_(0762E284).mkv", DEST, 1, [8]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_09_(F97788DE).mkv", DEST, 1, [9]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_10_(C4865F76).mkv", DEST, 1, [10]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_11_(17A90736).mkv", DEST, 1, [11]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_12_(B6A2FEDD).mkv", DEST, 1, [12]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_13_(EBD35F33).mkv", DEST, 1, [13]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_14_(7A6FCFF0).mkv", DEST, 1, [14]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_15_(E2D438F1).mkv", DEST, 1, [15]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_16_(85855E3D).mkv", DEST, 1, [16]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_17_(6645A201).mkv", DEST, 1, [17]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_18_(EE04B58B).mkv", DEST, 1, [18]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_19_(A7D9901B).mkv", DEST, 1, [19]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_20_(AB03EBAA).mkv", DEST, 1, [20]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_21_(329A47D2).mkv", DEST, 1, [21]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_22_(A72190BC).mkv", DEST, 1, [22]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_23_(16BEE764).mkv", DEST, 1, [23]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_24_(1C2CF777).mkv", DEST, 1, [24]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_25_(5251C88C).mkv", DEST, 1, [25]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_26_(F81C6DAB).mkv", DEST, 1, [26]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_27_(F408A8E7).mkv", DEST, 1, [27]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_28_(907E39C1).mkv", DEST, 1, [28]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_29_(63393467).mkv", DEST, 1, [29]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_30_(6CBA2D5E).mkv", DEST, 1, [30]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_31_(9F6095E2).mkv", DEST, 1, [31]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_32_(74E872DD).mkv", DEST, 1, [32]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_33_(41BE2AE0).mkv", DEST, 1, [33]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_34_(6542E685).mkv", DEST, 1, [34]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_35_(2312AAA5).mkv", DEST, 1, [35]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_36_(B27B9F64).mkv", DEST, 1, [36]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_37_(EBC5748A).mkv", DEST, 1, [37]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_38_(0FED2307).mkv", DEST, 1, [38]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_39_(8B8A1637).mkv", DEST, 1, [39]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_40_(9B0129F7).mkv", DEST, 1, [40]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_41_(8FA07092).mkv", DEST, 1, [41]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_42_(C6131024).mkv", DEST, 1, [42]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_43_(F0D2DC67).mkv", DEST, 1, [43]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_44_(F8EEEB53).mkv", DEST, 1, [44]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_45_(C4C72095).mkv", DEST, 1, [45]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_46_(09FBCE54).mkv", DEST, 1, [46]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_47_(DF039408).mkv", DEST, 1, [47]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_48_(4CFB8F80).mkv", DEST, 1, [48]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_49_(943F5A1C).mkv", DEST, 1, [49]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_50_(38C0B94D).mkv", DEST, 1, [50]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_51_(7DD94D9F).mkv", DEST, 1, [51]),
    ("[Bunny_Hat_Raw]Battle_Fever_J_52_(73B53040).mkv", DEST, 1, [52]),
    # Movie → Season 0
    ("[Bunny_Hat_Raw]Battle_Fever_J_Movie_(E0479B92).mkv", DEST, 0, [1]),
]


def _show_name(dest_root): return dest_root.name
def _ep_tag(episodes): return "".join(f"E{e:02d}" for e in episodes)

def _dest_path(dest_root, season, episodes, ext=".mkv"):
    show = _show_name(dest_root)
    ep_tag = _ep_tag(episodes)
    fname = f"{show} - S{season:02d}{ep_tag}{ext}"
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
