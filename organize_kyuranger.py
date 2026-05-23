from pathlib import Path
import os, shutil, logging, argparse

logging.basicConfig(level=logging.INFO, format="%(levelname)s  %(message)s")

# TheTVDB uses "Uchu Sentai Kyuranger" (simplified spelling).
# Episodes 03 and 12 are missing from this collection.
# Episode 07 is HD720 quality; episodes 17 and 45 are SD-only.
SOURCE = Path("/media/madmaxlgndklr/media31/Shows/Uchuu Sentai Kyuuranger")
DEST   = Path("/media/madmaxlgndklr/media31/Shows/Uchu Sentai Kyuranger (2017)")

MANIFEST = [
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_01[F52392D2].mp4",          DEST, 1, [1]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_02v2[1D9EECB8].mp4",        DEST, 1, [2]),
    # ep 03 missing
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_04[E6CCC2DE].mp4",          DEST, 1, [4]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_05[44B34C0C].mp4",          DEST, 1, [5]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_06[4AF13998].mp4",          DEST, 1, [6]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD720_07[D8679F7B].mp4",       DEST, 1, [7]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_08[89615761].mp4",          DEST, 1, [8]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_09[A113D76B].mp4",          DEST, 1, [9]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_10[679B0BFB].mp4",          DEST, 1, [10]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_11[729B79D0].mp4",          DEST, 1, [11]),
    # ep 12 missing
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_13[68F55694].mp4",          DEST, 1, [13]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_14[71EA6AAD].mp4",          DEST, 1, [14]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_15[74677654].mp4",          DEST, 1, [15]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_16v2[39C754ED].mp4",        DEST, 1, [16]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_SD_17v2[667B9827].mp4",        DEST, 1, [17]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_18[DA6BBFC1].mp4",          DEST, 1, [18]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_19[76064CF0].mp4",          DEST, 1, [19]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_20[D413019E].mp4",          DEST, 1, [20]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_21[B621B97F].mp4",          DEST, 1, [21]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_22[1CDFCBFF].mp4",          DEST, 1, [22]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_23v2[176A2FA2].mp4",        DEST, 1, [23]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_24[5EAE9B84].mp4",          DEST, 1, [24]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_25[97D324ED].mp4",          DEST, 1, [25]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_26[0FE1D56D].mp4",          DEST, 1, [26]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_27v2[E9D6D4D0].mp4",        DEST, 1, [27]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_28[ECE81361].mp4",          DEST, 1, [28]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_29[6605F405].mp4",          DEST, 1, [29]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_30[F4D38B1D].mp4",          DEST, 1, [30]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_31[792114E3].mp4",          DEST, 1, [31]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_32[BE4AC446].mp4",          DEST, 1, [32]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_33v2[67A8B8B4].mp4",        DEST, 1, [33]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_34[DDC14803].mp4",          DEST, 1, [34]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_35[220137A9].mp4",          DEST, 1, [35]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_36v2[5B0B08D2].mp4",        DEST, 1, [36]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_37v2[6BBE33A6].mp4",        DEST, 1, [37]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_38[577E855E].mp4",          DEST, 1, [38]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_39[4253E8CE].mp4",          DEST, 1, [39]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_40[919ADB12].mp4",          DEST, 1, [40]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_41[9717E98F].mp4",          DEST, 1, [41]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_42[5D14ACFC].mp4",          DEST, 1, [42]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_43[2017364E].mp4",          DEST, 1, [43]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_44[D129E44A].mp4",          DEST, 1, [44]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_SD_45[A81CFE22].mp4",          DEST, 1, [45]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_46[AD012BF7].mp4",          DEST, 1, [46]),
    ("[T-N]Uchuu_Sentai_KyuuRanger_HD_47[D4A51294].mp4",          DEST, 1, [47]),
    # Movie → Season 0
    ("[T-N]Uchuu_Sentai_KyuuRanger_HDBlu_Movie[568AE5D7].mp4",    DEST, 0, [1]),
]


def _show_name(dest_root): return dest_root.name
def _ep_tag(episodes): return "".join(f"E{e:02d}" for e in episodes)

def _dest_path(dest_root, season, episodes, ext=".mp4"):
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
