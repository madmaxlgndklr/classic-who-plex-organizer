from pathlib import Path
import os, shutil, logging, argparse

logging.basicConfig(level=logging.INFO, format="%(levelname)s  %(message)s")

SOURCE = Path("/media/madmaxlgndklr/media31/Shows/High-Speed Squad Turboranger")
DEST   = Path("/media/madmaxlgndklr/media31/Shows/Kousoku Sentai Turboranger (1989)")

MANIFEST = [
    # Season 0 — pre-series special
    ("[Bunny_Hat_Raw]Turboranger_00_(64D35DA9).mkv", DEST, 0, [0]),
    # Season 1 — episodes 1–51
    ("[Bunny_Hat_Raw]Turboranger_01_(293C4018).mkv", DEST, 1, [1]),
    ("[Bunny_Hat_Raw]Turboranger_02_(E6391035).mkv", DEST, 1, [2]),
    ("[Bunny_Hat_Raw]Turboranger_03_(61ED56FE).mkv", DEST, 1, [3]),
    ("[Bunny_Hat_Raw]Turboranger_04_(C5F9D715).mkv", DEST, 1, [4]),
    ("[Bunny_Hat_Raw]Turboranger_05_(B8BA074F).mkv", DEST, 1, [5]),
    ("[Bunny_Hat_Raw]Turboranger_06_(C5251BF9).mkv", DEST, 1, [6]),
    ("[Bunny_Hat_Raw]Turboranger_07_(E5B838CC).mkv", DEST, 1, [7]),
    ("[Bunny_Hat_Raw]Turboranger_08_(93020803).mkv", DEST, 1, [8]),
    ("[Bunny_Hat_Raw]Turboranger_09_(F7221715).mkv", DEST, 1, [9]),
    ("[Bunny_Hat_Raw]Turboranger_10_(12E94A7A).mkv", DEST, 1, [10]),
    ("[Bunny_Hat_Raw]Turboranger_11_(57CB0DB8).mkv", DEST, 1, [11]),
    ("[Bunny_Hat_Raw]Turboranger_12_(5D51AF36).mkv", DEST, 1, [12]),
    ("[Bunny_Hat_Raw]Turboranger_13_(5A55A948).mkv", DEST, 1, [13]),
    ("[Bunny_Hat_Raw]Turboranger_14_(8A40E113).mkv", DEST, 1, [14]),
    ("[Bunny_Hat_Raw]Turboranger_15_(30919CE7).mkv", DEST, 1, [15]),
    ("[Bunny_Hat_Raw]Turboranger_16_(B996FBC5).mkv", DEST, 1, [16]),
    ("[Bunny_Hat_Raw]Turboranger_17_(96B2C65C).mkv", DEST, 1, [17]),
    ("[Bunny_Hat_Raw]Turboranger_18_(53805CBF).mkv", DEST, 1, [18]),
    ("[Bunny_Hat_Raw]Turboranger_19_(F014E0F5).mkv", DEST, 1, [19]),
    ("[Bunny_Hat_Raw]Turboranger_20_(41BEF4B8).mkv", DEST, 1, [20]),
    ("[Bunny_Hat_Raw]Turboranger_21_(77DCD822).mkv", DEST, 1, [21]),
    ("[Bunny_Hat_Raw]Turboranger_22_(AFD2F5A0).mkv", DEST, 1, [22]),
    ("[Bunny_Hat_Raw]Turboranger_23_(C28EFC94).mkv", DEST, 1, [23]),
    ("[Bunny_Hat_Raw]Turboranger_24_(4E8ECFA5).mkv", DEST, 1, [24]),
    ("[Bunny_Hat_Raw]Turboranger_25_(DD7A8189).mkv", DEST, 1, [25]),
    ("[Bunny_Hat_Raw]Turboranger_26_(E7D093CE).mkv", DEST, 1, [26]),
    ("[Bunny_Hat_Raw]Turboranger_27_(D6B4A62C).mkv", DEST, 1, [27]),
    ("[Bunny_Hat_Raw]Turboranger_28_(A0686279).mkv", DEST, 1, [28]),
    ("[Bunny_Hat_Raw]Turboranger_29_(47B2F127).mkv", DEST, 1, [29]),
    ("[Bunny_Hat_Raw]Turboranger_30_(56AE1877).mkv", DEST, 1, [30]),
    ("[Bunny_Hat_Raw]Turboranger_31_(5627CB8B).mkv", DEST, 1, [31]),
    ("[Bunny_Hat_Raw]Turboranger_32_(7FF4A109).mkv", DEST, 1, [32]),
    ("[Bunny_Hat_Raw]Turboranger_33_(F2119399).mkv", DEST, 1, [33]),
    ("[Bunny_Hat_Raw]Turboranger_34_(C41C51F7).mkv", DEST, 1, [34]),
    ("[Bunny_Hat_Raw]Turboranger_35_(501B7F03).mkv", DEST, 1, [35]),
    ("[Bunny_Hat_Raw]Turboranger_36_(E0836337).mkv", DEST, 1, [36]),
    ("[Bunny_Hat_Raw]Turboranger_37_(B768AA73).mkv", DEST, 1, [37]),
    ("[Bunny_Hat_Raw]Turboranger_38_(8E88F187).mkv", DEST, 1, [38]),
    ("[Bunny_Hat_Raw]Turboranger_39_(FFC82D13).mkv", DEST, 1, [39]),
    ("[Bunny_Hat_Raw]Turboranger_40_(52305984).mkv", DEST, 1, [40]),
    ("[Bunny_Hat_Raw]Turboranger_41_(0AA166F4).mkv", DEST, 1, [41]),
    ("[Bunny_Hat_Raw]Turboranger_42_(10A2CF1E).mkv", DEST, 1, [42]),
    ("[Bunny_Hat_Raw]Turboranger_43_(FFBD4EB2).mkv", DEST, 1, [43]),
    ("[Bunny_Hat_Raw]Turboranger_44_(83A6F8EC).mkv", DEST, 1, [44]),
    ("[Bunny_Hat_Raw]Turboranger_45_(A39360AD).mkv", DEST, 1, [45]),
    ("[Bunny_Hat_Raw]Turboranger_46_(75502D49).mkv", DEST, 1, [46]),
    ("[Bunny_Hat_Raw]Turboranger_47_(79E8D5C0).mkv", DEST, 1, [47]),
    ("[Bunny_Hat_Raw]Turboranger_48_(A7F13BFB).mkv", DEST, 1, [48]),
    ("[Bunny_Hat_Raw]Turboranger_49_(1EDBFDBB).mkv", DEST, 1, [49]),
    ("[Bunny_Hat_Raw]Turboranger_50_(AB6AA511).mkv", DEST, 1, [50]),
    ("[Bunny_Hat_Raw]Turboranger_51_(124EA453).mkv", DEST, 1, [51]),
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
