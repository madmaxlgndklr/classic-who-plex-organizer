from pathlib import Path
import os, shutil, logging, argparse

logging.basicConfig(level=logging.INFO, format="%(levelname)s  %(message)s")

SOURCE = Path("/media/madmaxlgndklr/media31/Shows/Spec-Ops Cell Go-Busters")
DEST   = Path("/media/madmaxlgndklr/media31/Shows/Tokumei Sentai Go-Busters (2012)")

MANIFEST = [
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_01_[2798D8A8].mkv",  DEST, 1, [1]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_02_[5AEC5529].mkv",  DEST, 1, [2]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_03_[AED54055].mkv",  DEST, 1, [3]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_04_[E8AFE846].mkv",  DEST, 1, [4]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_05_[888B7003].mkv",  DEST, 1, [5]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_06_[0A75DCF3].mkv",  DEST, 1, [6]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_07_[C51E44A5].mkv",  DEST, 1, [7]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_08_[0824A739].mkv",  DEST, 1, [8]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_09_[9C1E937E].mkv",  DEST, 1, [9]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_10_[9CA497A2].mkv",  DEST, 1, [10]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_11_[32477145].mkv",  DEST, 1, [11]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_12_[EBC58D32].mkv",  DEST, 1, [12]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_13_[D0CBE174].mkv",  DEST, 1, [13]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_14_[56F12659].mkv",  DEST, 1, [14]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_15_[44EDC267].mkv",  DEST, 1, [15]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_16_[1CAE948F].mkv",  DEST, 1, [16]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_17_[4993881D].mkv",  DEST, 1, [17]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_18_[280AE702].mkv",  DEST, 1, [18]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_19_[FEDBF629].mkv",  DEST, 1, [19]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_20_[AB50C327].mkv",  DEST, 1, [20]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_21_[FF4985EE].mkv",  DEST, 1, [21]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_22v2_[251EA69C].mkv", DEST, 1, [22]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_23_[CFC5F408].mkv",  DEST, 1, [23]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_24_[F1442E58].mkv",  DEST, 1, [24]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_25_[FB45B58C].mkv",  DEST, 1, [25]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_26_[7FF846FB].mkv",  DEST, 1, [26]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_27_[EC5E43BD].mkv",  DEST, 1, [27]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_28_[B13E0A94].mkv",  DEST, 1, [28]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_29_[BADB477C].mkv",  DEST, 1, [29]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_30_[81BB5322].mkv",  DEST, 1, [30]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_31_[96ED393C].mkv",  DEST, 1, [31]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_32_[80C65563].mkv",  DEST, 1, [32]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_33_[A5F7D234].mkv",  DEST, 1, [33]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_34_[B2B9BC18].mkv",  DEST, 1, [34]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_35_[33781C3D].mkv",  DEST, 1, [35]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_36_[CF4BDB06].mkv",  DEST, 1, [36]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_37_[F9C88803].mkv",  DEST, 1, [37]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_38_[30756D61].mkv",  DEST, 1, [38]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_39_[6448AE6F].mkv",  DEST, 1, [39]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_40_[5BB91310].mkv",  DEST, 1, [40]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_41_[3CD55640].mkv",  DEST, 1, [41]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_42_[AD678EE1].mkv",  DEST, 1, [42]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_43_[F6464262].mkv",  DEST, 1, [43]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_44_[DE878CEE].mkv",  DEST, 1, [44]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_45_[AB44BA57].mkv",  DEST, 1, [45]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_46_[9B1218FF].mkv",  DEST, 1, [46]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_47_[86EDEAE5].mkv",  DEST, 1, [47]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_48_[4C2AD966].mkv",  DEST, 1, [48]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_49_[75D5B5F2].mkv",  DEST, 1, [49]),
    ("[Over-Time]_Spec-Ops_Cell_Go-Busters_-_50_[61E45567].mkv",  DEST, 1, [50]),
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
