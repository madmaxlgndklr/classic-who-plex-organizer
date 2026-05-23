from pathlib import Path
import os, shutil, argparse, logging

# ── Step 1: Set your paths ─────────────────────────────────────────────────
# SOURCE: directory where your video files currently live
# DEST:   Plex show folder — Plex expects "Season XX" subdirectories inside

SOURCE = Path("/path/to/your/source/directory")
DEST   = Path("/path/to/plex/Show Name (Year)")

# For shows split into multiple Plex entries (e.g. a franchise spanning two
# separate series), define additional DEST constants and reference them in
# MANIFEST below. Example:
#   DEST_B = Path("/path/to/plex/Show Name Sequel Series")

# ── Step 2: Fill in MANIFEST ──────────────────────────────────────────────
# Each row: (source_filename, dest_root, season, [episode_numbers], display_title)
#
#   source_filename   exact filename in SOURCE (including extension)
#   dest_root         which DEST constant this file belongs under
#   season            integer season number
#   episode_numbers   list of episode numbers covered by this single file
#   display_title     episode title as it should appear in the Plex filename
#
# Single-episode file:
#   ("Show - 1x01.avi",      DEST, 1, [1],    "Pilot")
#
# Multi-episode file (e.g. a two-parter stored in one file):
#   ("Show - 1x03-04.avi",   DEST, 1, [3, 4], "Two-Part Episode Title")
#
# Split-show file (going to a different DEST):
#   ("Show - 2x01.avi",      DEST_B, 1, [1],  "New Series Premiere")
#
# Output filename format:
#   Show Name (Year) - S01E01 - Pilot.avi
#   Show Name (Year) - S01E03E04 - Two-Part Episode Title.avi

MANIFEST = [
    # ── Season 1 ──────────────────────────────────────────────────────────
    # ("S01E01 - Pilot.avi",              DEST, 1, [1],    "Pilot"),
    # ("S01E02 - Second Episode.avi",     DEST, 1, [2],    "Second Episode"),
    # ("S01E03E04 - Two Parter.avi",      DEST, 1, [3, 4], "Two-Part Episode"),
    # ── Season 2 ──────────────────────────────────────────────────────────
    # ("S02E01 - Season Opener.avi",      DEST, 2, [1],    "Season Opener"),
]


def _show_name(dest_root: Path) -> str:
    return dest_root.name


def _ep_tag(episodes: list) -> str:
    return "".join(f"E{e:02d}" for e in episodes)


def _dest_path(dest_root: Path, season: int, episodes: list, title: str, ext: str = ".avi") -> Path:
    show = _show_name(dest_root)
    fname = f"{show} - S{season:02d}{_ep_tag(episodes)} - {title}{ext}"
    return dest_root / f"Season {season:02d}" / fname


def build_plan() -> list:
    moves = []
    for src_name, dest_root, season, episodes, title in MANIFEST:
        src = SOURCE / src_name
        dest = _dest_path(dest_root, season, episodes, title, Path(src_name).suffix)
        moves.append((src, dest))
    return moves


def execute_plan(moves: list, dry_run: bool = True) -> tuple:
    moved = skipped = errors = 0
    for src, dest in moves:
        if not src.exists():
            logging.warning(f"WARN  source missing: {src.name}")
            errors += 1
            continue
        if dest.exists():
            logging.info(f"SKIP  {dest.name}")
            skipped += 1
            continue
        if dry_run:
            logging.info(f"DRY   {src.name}\n   -> {dest}")
            moved += 1
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            try:
                os.rename(src, dest)
            except OSError:
                shutil.move(str(src), str(dest))
            logging.info(f"MOVE  {src.name}\n   -> {dest}")
            moved += 1
    return moved, skipped, errors


def main():
    parser = argparse.ArgumentParser(description="Reorganize series files for Plex")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true")
    group.add_argument("--execute", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("organize_series.log"),
        ],
    )

    moves = build_plan()
    logging.info(f"\nPlan: {len(moves)} file operations")
    moved, skipped, errors = execute_plan(moves, dry_run=not args.execute)
    logging.info(f"\nSummary: moved={moved}  skipped={skipped}  errors={errors}")


if __name__ == "__main__":
    main()
