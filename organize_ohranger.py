from pathlib import Path
import os, shutil, logging, argparse

logging.basicConfig(level=logging.INFO, format="%(levelname)s  %(message)s")

# Files already have S19E## naming (Super Sentai season 19).
# Mapping them to standalone show S01E## so Plex matches Chouriki Sentai Ohranger directly.
SOURCE = Path("/media/madmaxlgndklr/media31/Shows/Ohranger")
DEST   = Path("/media/madmaxlgndklr/media31/Shows/Chouriki Sentai Ohranger (1995)")

MANIFEST = [
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E01 - Invasion!! 1999 (1995) (DVD).mkv",                     DEST, 1, [1]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E02 - Assemble!! Chouriki Sentai (1995) (DVD).mkv",          DEST, 1, [2]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E03 - Crisis- The Secret of Chouriki (1995) (DVD).mkv",      DEST, 1, [3]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E04 - Bizarre!! Iron Man Papa (1995) (DVD).mkv",             DEST, 1, [4]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E05 - Fierce Love!! The Burning Brothers (1995) (DVD).mkv",  DEST, 1, [5]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E06 - Formidable Foe- A Thinking Machine (1995) (DVD).mkv",  DEST, 1, [6]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E07 - Complete!! The Chouriki Robo! (1995) (DVD).mkv",       DEST, 1, [7]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E08 - Clash!! A Sudden Giant Battle (1995) (DVD).mkv",       DEST, 1, [8]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E09 - Suddenly!! A Traitor (1995) (DVD).mkv",                DEST, 1, [9]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E10 - Here I Am, I'm a Burglar (1995) (DVD).mkv",            DEST, 1, [10]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E11 - Submit- The Refrigerator of Love (1995) (DVD).mkv",    DEST, 1, [11]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E12 - Explosion!! A Baby (1995) (DVD).mkv",                  DEST, 1, [12]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E13 - Illusion- The Dog of the Gods (1995) (DVD).mkv",       DEST, 1, [13]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E14 - I Love Pinnochio (1995) (DVD).mkv",                    DEST, 1, [14]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E15 - My Friend, Rest in Passion!! (1995) (DVD).mkv",        DEST, 1, [15]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E16 - Naughty!! The Future Child (1995) (DVD).mkv",          DEST, 1, [16]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E17 - The Stolen Transformation Brace (1995) (DVD).mkv",     DEST, 1, [17]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E18 - Dad's Unusual Love (1995) (DVD).mkv",                  DEST, 1, [18]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E19 - The New Robo's Red Impact (1995) (DVD).mkv",           DEST, 1, [19]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E20 - Iron Fist 100 Bursts!! (1995) (DVD).mkv",              DEST, 1, [20]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E21 - The Storm-Calling Kendama (1995) (DVD).mkv",           DEST, 1, [21]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E22 - The Classified Combination Order!! (1995) (DVD).mkv",  DEST, 1, [22]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E23 - The Final Swimsuit... (1995) (DVD).mkv",               DEST, 1, [23]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E24 - The Laughing Nostalgic Man!! (1995) (DVD).mkv",        DEST, 1, [24]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E25 - The Festival One-Shot Contest! (1995) (DVD).mkv",      DEST, 1, [25]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E26 - The 600-Million-Year-Old Boy Warrior(1995) (DVD).mkv", DEST, 1, [26]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E27 - King's Gallant Debut (1995) (DVD).mkv",                DEST, 1, [27]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E28 - Behold, The Miracle Fortress (1995) (DVD).mkv",        DEST, 1, [28]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E29 - Dance!  The Invasion Cram School!! (1995) (DVD).mkv",  DEST, 1, [29]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E30 - The Earth's Sleeping Like a Log(1995) (DVD).mkv",      DEST, 1, [30]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E31 - Home Delivery Diet (1995) (DVD).mkv",                  DEST, 1, [31]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E32 - The Terrifying School Nightmare (1995) (DVD).mkv",     DEST, 1, [32]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E33 - The Five Robos' Rampage (1995) (DVD).mkv",             DEST, 1, [33]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E34 - The Emperor's Final Challenge (1995) (DVD).mkv",       DEST, 1, [34]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E35 - The Violently Explosive Jerk (1995) (DVD).mkv",        DEST, 1, [35]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E36 - A Direct Hit With Flatulence!! (1995) (DVD).mkv",      DEST, 1, [36]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E37 - I am Gunmajin! (1995) (DVD).mkv",                      DEST, 1, [37]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E38 - It's Tough Being a Majin! (1995) (DVD).mkv",           DEST, 1, [38]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E39 - The Prince Dies In A Duel (1995) (DVD).mkv",           DEST, 1, [39]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E40 - Arrival! The Mysterious Princess!! (1995) (DVD).mkv",  DEST, 1, [40]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E41 - The Dangerous Couple!! (1995) (DVD).mkv",              DEST, 1, [41]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E42 - The Squadron's Public Execution!! (1996) (DVD).mkv",   DEST, 1, [42]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E43 - The Trump Card is Seven Changes (1996) (DVD).mkv",     DEST, 1, [43]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E44 - The Strongest Beauty on Earth (1996) (DVD).mkv",       DEST, 1, [44]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E45 - Destruction!! The Chouriki Base (1996) (DVD).mkv",     DEST, 1, [45]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E46 - Earth's Final Day!! (1996) (DVD).mkv",                 DEST, 1, [46]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E47 - Rise, Shine, Be Reborn!! (1996) (DVD).mkv",            DEST, 1, [47]),
    ("[PocketUniverse] Chouriki Sentai Ohranger - S19E48 - The Heroes of Love (1996) (DVD).mkv",                  DEST, 1, [48]),
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
