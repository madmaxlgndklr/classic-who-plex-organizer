from pathlib import Path
import os, shutil, argparse, logging

SOURCE = Path("/media/madmaxlgndklr/media31/Shows/Dragonball Z")
DEST   = Path("/media/madmaxlgndklr/media31/Shows/Dragonball Z")

# Partial collection: FUNimation sequential episodes 198–276 (Buu Saga).
# Season boundaries follow FUNimation's 9-season DVD release structure:
#   S07: eps 195–219  |  S08: eps 220–253  |  S09: eps 254–291
# Our files cover S07E04–S07E25, full S08, and S09E01–S09E23.
MANIFEST = [
    # ── Season 7 (World Tournament / Babidi / Majin Buu unleashed) ────────
    ("DBZ - 198 Big Trouble, Little Trunks.avi",       DEST, 7, [4],  "Big Trouble, Little Trunks"),
    ("DBZ - 199 Who Will Fight Who.avi",                DEST, 7, [5],  "Who Will Fight Who"),
    ("DBZ - 200 Forfeit Of Piccolo.avi",                DEST, 7, [6],  "Forfeit of Piccolo"),
    ("DBZ - 201 A Dark And Secret Power.avi",           DEST, 7, [7],  "A Dark and Secret Power"),
    ("DBZ - 202 Videl Is Crushed.avi",                  DEST, 7, [8],  "Videl Is Crushed"),
    ("DBZ - 203 Identities Revealed.avi",               DEST, 7, [9],  "Identities Revealed"),
    ("DBZ - 204 Energy Drain.avi",                      DEST, 7, [10], "Energy Drain"),
    ("DBZ - 205 - The Wizards Curse.avi",               DEST, 7, [11], "The Wizard's Curse"),
    ("DBZ - 206 - King Of The Demons.avi",              DEST, 7, [12], "King of the Demons"),
    ("DBZ - 207 Vegeta attacks.avi",                    DEST, 7, [13], "Vegeta Attacks"),
    ("DBZ - 208 Next Up Goku.avi",                      DEST, 7, [14], "Next Up, Goku"),
    ("DBZ - 209 Battle Supreme.avi",                    DEST, 7, [15], "Battle Supreme"),
    ("DBZ - 210 Eighteen Unmasks.avi",                  DEST, 7, [16], "Eighteen Unmasks"),
    ("DBZ - 211 - Pay To Win.avi",                      DEST, 7, [17], "Pay to Win"),
    ("DBZ - 212 - Heart of a Villain.avi",              DEST, 7, [18], "Heart of a Villain"),
    ("DBZ - 213 The Dark Prince Returns.avi",           DEST, 7, [19], "The Dark Prince Returns"),
    ("DBZ - 214 - Vegeta's Pride.avi",                  DEST, 7, [20], "Vegeta's Pride"),
    ("DBZ - 215 The Long Awaited Fight.avi",            DEST, 7, [21], "The Long Awaited Fight"),
    ("DBZ - 216 Magic Ball Of Buu.avi",                 DEST, 7, [22], "Magic Ball of Buu"),
    ("DBZ - 217 Buu Is Hatched.avi",                    DEST, 7, [23], "Buu Is Hatched"),
    ("DBZ - 218 The Losses Begin.avi",                  DEST, 7, [24], "The Losses Begin"),
    ("DBZ - 219 The Terror of Mr. Buu.avi",             DEST, 7, [25], "The Terror of Mr. Buu"),
    # ── Season 8 (Fusion / Super Buu) ─────────────────────────────────────
    ("DBZ - 220 Meal Time.avi",                         DEST, 8, [1],  "Meal Time"),
    ("DBZ - 221 - The Warriors Decision.avi",           DEST, 8, [2],  "The Warrior's Decision"),
    ("DBZ - 222 Final Atonement.avi",                   DEST, 8, [3],  "Final Atonement"),
    ("DBZ - 223 Evil Lives On.avi",                     DEST, 8, [4],  "Evil Lives On"),
    ("DBZ - 224 - Find The Dragonballs [AHQ].avi",      DEST, 8, [5],  "Find the Dragonballs"),
    ("DBZ - 225 Revival.avi",                           DEST, 8, [6],  "Revival"),
    ("DBZ - 226 Global Announcement.avi",               DEST, 8, [7],  "Global Announcement"),
    ("DBZ - 227 Learn To Fuse.avi",                     DEST, 8, [8],  "Learn to Fuse"),
    ("DBZ - 228 The Z Sword.avi",                       DEST, 8, [9],  "The Z Sword"),
    ("DBZ - 229 Race To Capsule Corp.avi",              DEST, 8, [10], "Race to Capsule Corp"),
    ("DBZ - 230 Super Saiyan 3.avi",                    DEST, 8, [11], "Super Saiyan 3"),
    ("DBZ - 231 Buu's Mutiny.avi",                      DEST, 8, [12], "Buu's Mutiny"),
    ("DBZ - 232 The Fusion Dance.avi",                  DEST, 8, [13], "The Fusion Dance"),
    ("DBZ - 233 Goku's Time Is Up.avi",                 DEST, 8, [14], "Goku's Time Is Up"),
    ("DBZ - 234 Return To The Other World.avi",         DEST, 8, [15], "Return to the Other World"),
    ("DBZ - 235 Out From The Broken Sword.avi",         DEST, 8, [16], "Out From the Broken Sword"),
    ("DBZ - 236 Gotenks Is Born.avi",                   DEST, 8, [17], "Gotenks Is Born"),
    ("DBZ - 237 Unlikely Friendship.avi",               DEST, 8, [18], "Unlikely Friendship"),
    ("DBZ - 238 I Kill No More.avi",                    DEST, 8, [19], "I Kill No More"),
    ("DBZ - 239 The Evil Of Men.avi",                   DEST, 8, [20], "The Evil of Men"),
    ("DBZ - 240 Buu Against Buu.avi",                   DEST, 8, [21], "Buu Against Buu"),
    ("DBZ - 241 Empty Planet.avi",                      DEST, 8, [22], "Empty Planet"),
    ("DBZ - 242 Time Struggle.avi",                     DEST, 8, [23], "Time Struggle"),
    ("DBZ - 243 Super Moves Of Gotenks.avi",            DEST, 8, [24], "Super Moves of Gotenks"),
    ("DBZ - 244 Trapped In Forever.avi",                DEST, 8, [25], "Trapped in Forever"),
    ("DBZ - 245 Feeding Frenzy.avi",                    DEST, 8, [26], "Feeding Frenzy"),
    ("DBZ - 246 Gotenks Is Awesome!.avi",               DEST, 8, [27], "Gotenks Is Awesome!"),
    ("DBZ - 247 Unlucky Break.avi",                     DEST, 8, [28], "Unlucky Break"),
    ("DBZ - 248 A Whole New Gohan.avi",                 DEST, 8, [29], "A Whole New Gohan"),
    ("DBZ - 249 Search For Survivors.avi",              DEST, 8, [30], "Search for Survivors"),
    ("DBZ - 250 Majin Buu Transforms.avi",              DEST, 8, [31], "Majin Buu Transforms"),
    ("DBZ - 251The Old Kai's Weapon.avi",               DEST, 8, [32], "The Old Kai's Weapon"),
    ("DBZ - 252 Ready To Fuse.avi",                     DEST, 8, [33], "Ready to Fuse"),
    ("DBZ - 253 Union Of Rivals.avi",                   DEST, 8, [34], "Union of Rivals"),
    # ── Season 9 (Kid Buu / End) ──────────────────────────────────────────
    ("DBZ - 254 Meet Vegito.avi",                       DEST, 9, [1],  "Meet Vegito"),
    ("DBZ - 255 Rip In the Universe.avi",               DEST, 9, [2],  "Rip in the Universe"),
    ("DBZ - 256 Vegito..... Downsized.avi",             DEST, 9, [3],  "Vegito... Downsized"),
    ("DBZ - 257 The Incredible Fighting Candy.avi",     DEST, 9, [4],  "The Incredible Fighting Candy"),
    ("DBZ - 258 The Innards Of Buu.avi",                DEST, 9, [5],  "The Innards of Buu"),
    ("DBZ - 259 Mind Trap.avi",                         DEST, 9, [6],  "Mind Trap"),
    ("DBZ - 260 Deadly Vision.avi",                     DEST, 9, [7],  "Deadly Vision"),
    ("DBZ - 261 - Evil Kid Buu.avi",                    DEST, 9, [8],  "Evil Kid Buu"),
    ("DBZ - 262 End of Earth.avi",                      DEST, 9, [9],  "End of Earth"),
    ("DBZ - 263 True Saiyans Fight Alone.avi",          DEST, 9, [10], "True Saiyans Fight Alone"),
    ("DBZ - 264 Battle For The Universe Begins.avi",    DEST, 9, [11], "Battle for the Universe Begins"),
    ("DBZ - 265 Vegeta's Respect.avi",                  DEST, 9, [12], "Vegeta's Respect"),
    ("DBZ - 266 Minute Of Desperation.avi",             DEST, 9, [13], "Minute of Desperation"),
    ("DBZ - 267 Old Buu Emerges.avi",                   DEST, 9, [14], "Old Buu Emerges"),
    ("DBZ - 268 Earth Reborn.avi",                      DEST, 9, [15], "Earth Reborn"),
    ("DBZ - 269 Call To Action.avi",                    DEST, 9, [16], "Call to Action"),
    ("DBZ - 270 People Of Earth Unite.avi",             DEST, 9, [17], "People of Earth Unite"),
    ("DBZ - 271 Spirit Bomb Triumphant.avi",            DEST, 9, [18], "Spirit Bomb Triumphant"),
    ("DBZ - 272 Celebrations With Majin Buu.avi",       DEST, 9, [19], "Celebrations with Majin Buu"),
    ("DBZ - 273 - He Is Always Late.avi",               DEST, 9, [20], "He Is Always Late"),
    ("DBZ - 274 Grandaughter Pan.avi",                  DEST, 9, [21], "Granddaughter Pan"),
    ("DBZ - 275 Buu's Reincarnation.avi",               DEST, 9, [22], "Buu's Reincarnation"),
    ("DBZ - 276 Goku's Next Journey.avi",               DEST, 9, [23], "Goku's Next Journey"),
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
    parser = argparse.ArgumentParser(description="Reorganize Dragon Ball Z files for Plex")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true")
    group.add_argument("--execute", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("organize_dragonball_z.log"),
        ],
    )

    moves = build_plan()
    logging.info(f"\nPlan: {len(moves)} file operations")
    moved, skipped, errors = execute_plan(moves, dry_run=not args.execute)
    logging.info(f"\nSummary: moved={moved}  skipped={skipped}  errors={errors}")


if __name__ == "__main__":
    main()
