from pathlib import Path
import os, shutil, logging, argparse

logging.basicConfig(level=logging.INFO, format="%(levelname)s  %(message)s")

# Source files are nested one level inside the Bunny Hat Raw subfolder.
SOURCE = Path("/media/madmaxlgndklr/media31/Shows/Abaranger/[Bunny Hat Raw]Burstosaur Squad Abaranger (DVD) (10-bit x264,AAC)")
DEST   = Path("/media/madmaxlgndklr/media31/Shows/Bakuryuu Sentai Abaranger (2003)")

MANIFEST = [
    # Episodes 1–50 only; extras (Free Talk, Inside Story, NCED/NCOP, Promos, etc.) left in source.
    ("[Bunny_Hat_Raw]Abaranger_01_(1CF1E267).mkv", DEST, 1, [1]),
    ("[Bunny_Hat_Raw]Abaranger_02_(6B6579D8).mkv", DEST, 1, [2]),
    ("[Bunny_Hat_Raw]Abaranger_03_(CCF86ADE).mkv", DEST, 1, [3]),
    ("[Bunny_Hat_Raw]Abaranger_04_(27F4910D).mkv", DEST, 1, [4]),
    ("[Bunny_Hat_Raw]Abaranger_05_(1F4D21C5).mkv", DEST, 1, [5]),
    ("[Bunny_Hat_Raw]Abaranger_06_(5AA5452B).mkv", DEST, 1, [6]),
    ("[Bunny_Hat_Raw]Abaranger_07_(DF69A565).mkv", DEST, 1, [7]),
    ("[Bunny_Hat_Raw]Abaranger_08_(8AA29CF2).mkv", DEST, 1, [8]),
    ("[Bunny_Hat_Raw]Abaranger_09_(7830C935).mkv", DEST, 1, [9]),
    ("[Bunny_Hat_Raw]Abaranger_10_(872400A3).mkv", DEST, 1, [10]),
    ("[Bunny_Hat_Raw]Abaranger_11_(68BBB6A9).mkv", DEST, 1, [11]),
    ("[Bunny_Hat_Raw]Abaranger_12_(3F8DFA79).mkv", DEST, 1, [12]),
    ("[Bunny_Hat_Raw]Abaranger_13_(56F8D31D).mkv", DEST, 1, [13]),
    ("[Bunny_Hat_Raw]Abaranger_14_(106A54D0).mkv", DEST, 1, [14]),
    ("[Bunny_Hat_Raw]Abaranger_15_(0BC8C216).mkv", DEST, 1, [15]),
    ("[Bunny_Hat_Raw]Abaranger_16_(E7560314).mkv", DEST, 1, [16]),
    ("[Bunny_Hat_Raw]Abaranger_17_(C92BCC26).mkv", DEST, 1, [17]),
    ("[Bunny_Hat_Raw]Abaranger_18_(6A58C341).mkv", DEST, 1, [18]),
    ("[Bunny_Hat_Raw]Abaranger_19_(B88337B1).mkv", DEST, 1, [19]),
    ("[Bunny_Hat_Raw]Abaranger_20_(2A927333).mkv", DEST, 1, [20]),
    ("[Bunny_Hat_Raw]Abaranger_21_(868FCDFC).mkv", DEST, 1, [21]),
    ("[Bunny_Hat_Raw]Abaranger_22_(F526E94A).mkv", DEST, 1, [22]),
    ("[Bunny_Hat_Raw]Abaranger_23_(AD76A0C3).mkv", DEST, 1, [23]),
    ("[Bunny_Hat_Raw]Abaranger_24_(D14459AE).mkv", DEST, 1, [24]),
    ("[Bunny_Hat_Raw]Abaranger_25_(2A6FE59D).mkv", DEST, 1, [25]),
    ("[Bunny_Hat_Raw]Abaranger_26_(5FCD9BCE).mkv", DEST, 1, [26]),
    ("[Bunny_Hat_Raw]Abaranger_27_(CD7D1B92).mkv", DEST, 1, [27]),
    ("[Bunny_Hat_Raw]Abaranger_28_(BE6308F4).mkv", DEST, 1, [28]),
    ("[Bunny_Hat_Raw]Abaranger_29_(CDB0FCA3).mkv", DEST, 1, [29]),
    ("[Bunny_Hat_Raw]Abaranger_30_(A23104CA).mkv", DEST, 1, [30]),
    ("[Bunny_Hat_Raw]Abaranger_31_(003360AC).mkv", DEST, 1, [31]),
    ("[Bunny_Hat_Raw]Abaranger_32_(E31D3B9A).mkv", DEST, 1, [32]),
    ("[Bunny_Hat_Raw]Abaranger_33_(857A8EEF).mkv", DEST, 1, [33]),
    ("[Bunny_Hat_Raw]Abaranger_34_(B70CB912).mkv", DEST, 1, [34]),
    ("[Bunny_Hat_Raw]Abaranger_35_(72C320DA).mkv", DEST, 1, [35]),
    ("[Bunny_Hat_Raw]Abaranger_36_(176E308E).mkv", DEST, 1, [36]),
    ("[Bunny_Hat_Raw]Abaranger_37_(09903BED).mkv", DEST, 1, [37]),
    ("[Bunny_Hat_Raw]Abaranger_38_(497F6463).mkv", DEST, 1, [38]),
    ("[Bunny_Hat_Raw]Abaranger_39_(71663FCA).mkv", DEST, 1, [39]),
    ("[Bunny_Hat_Raw]Abaranger_40_(AE41E01C).mkv", DEST, 1, [40]),
    ("[Bunny_Hat_Raw]Abaranger_41_(D6599F5E).mkv", DEST, 1, [41]),
    ("[Bunny_Hat_Raw]Abaranger_42_(297C5003).mkv", DEST, 1, [42]),
    ("[Bunny_Hat_Raw]Abaranger_43_(D47BD1B6).mkv", DEST, 1, [43]),
    ("[Bunny_Hat_Raw]Abaranger_44_(7EC7349D).mkv", DEST, 1, [44]),
    ("[Bunny_Hat_Raw]Abaranger_45_(CD0B086C).mkv", DEST, 1, [45]),
    ("[Bunny_Hat_Raw]Abaranger_46_(19A670E3).mkv", DEST, 1, [46]),
    ("[Bunny_Hat_Raw]Abaranger_47_(18CE335B).mkv", DEST, 1, [47]),
    ("[Bunny_Hat_Raw]Abaranger_48_(5E5188D3).mkv", DEST, 1, [48]),
    ("[Bunny_Hat_Raw]Abaranger_49_(6054D299).mkv", DEST, 1, [49]),
    ("[Bunny_Hat_Raw]Abaranger_50_(E3AC552E).mkv", DEST, 1, [50]),
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
