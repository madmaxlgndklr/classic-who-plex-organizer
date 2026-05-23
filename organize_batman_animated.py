from pathlib import Path
import os, shutil, argparse, logging

SOURCE = Path("/media/madmaxlgndklr/media22/shows/BATMAN The Animated Series Complete")
DEST   = Path("/media/madmaxlgndklr/media22/shows/Batman - The Animated Series (1992)")

# Season 1 = DVD Vol. 1–3 (85 original episodes, production order)
# Season 2 = DVD Vol. 4 (24 New Batman Adventures episodes)
# Five episodes also exist as higher-quality MKV files in the source root
# (S04E01–05 naming); those are included at their correct S01 positions,
# resulting in avi+mkv duplicates for those five episodes so the better
# copy can be kept after verifying playback.
MANIFEST = [
    # ── Season 1 — Vol. 1 (episodes 1–28) ────────────────────────────────
    ("Batman the Animated Series Vol. 1/01. On Leather Wings.xvid",            DEST, 1, [1],  "On Leather Wings"),
    ("Batman the Animated Series Vol. 1/02. Christmas with the Joker .xvid",   DEST, 1, [2],  "Christmas with the Joker"),
    ("Batman the Animated Series Vol. 1/03. Nothing to Fear.xvid",             DEST, 1, [3],  "Nothing to Fear"),
    ("Batman the Animated Series Vol. 1/04. The Last Laugh.xvid",              DEST, 1, [4],  "The Last Laugh"),
    ("Batman the Animated Series Vol. 1/05. Pretty Poison.xvid",               DEST, 1, [5],  "Pretty Poison"),
    ("Batman the Animated Series Vol. 1/06. The Underdwellers.xvid",           DEST, 1, [6],  "The Underdwellers"),
    ("Batman the Animated Series Vol. 1/07. P.O.V. .xvid",                     DEST, 1, [7],  "P.O.V."),
    ("Batman the Animated Series Vol. 1/08. Forgotten.xvid",                   DEST, 1, [8],  "Forgotten"),
    ("Batman the Animated Series Vol. 1/09. Be a Clown.xvid",                  DEST, 1, [9],  "Be a Clown"),
    ("Batman the Animated Series Vol. 1/10. Two-Face Part 1.xvid",             DEST, 1, [10], "Two-Face Part 1"),
    ("Batman the Animated Series Vol. 1/11. Two-Face Part 2.xvid",             DEST, 1, [11], "Two-Face Part 2"),
    ("Batman the Animated Series Vol. 1/12. It's Never Too Late.xvid",         DEST, 1, [12], "It's Never Too Late"),
    ("Batman the Animated Series Vol. 1/13. I've Got Batman in My Basement.xvid", DEST, 1, [13], "I've Got Batman in My Basement"),
    # 14.5 is a commentary track — skipped
    ("Batman the Animated Series Vol. 1/14. Heart of Ice.xvid",                DEST, 1, [14], "Heart of Ice"),
    ("Batman the Animated Series Vol. 1/15. Cat and Claw Part 1.xvid",         DEST, 1, [15], "Cat and Claw Part 1"),
    ("Batman the Animated Series Vol. 1/16. Cat and Claw Part 2.xvid",         DEST, 1, [16], "Cat and Claw Part 2"),
    ("Batman the Animated Series Vol. 1/17. See No Evil.xvid",                 DEST, 1, [17], "See No Evil"),
    ("Batman the Animated Series Vol. 1/18. Beware of Gray Ghost.xvid",        DEST, 1, [18], "Beware the Gray Ghost"),
    ("Batman the Animated Series Vol. 1/19. Prophecy of Doom.xvid",            DEST, 1, [19], "Prophecy of Doom"),
    ("Batman the Animated Series Vol. 1/20. Feat of Clay Part 1.xvid",         DEST, 1, [20], "Feat of Clay Part 1"),
    ("Batman the Animated Series Vol. 1/21. Feat of Clay Part 2.xvid",         DEST, 1, [21], "Feat of Clay Part 2"),
    ("Batman the Animated Series Vol. 1/22. Joker's Favor.xvid",               DEST, 1, [22], "Joker's Favor"),
    ("Batman the Animated Series Vol. 1/23. Vendetta.xvid",                    DEST, 1, [23], "Vendetta"),
    ("Batman the Animated Series Vol. 1/24. Fear of Victory.xvid",             DEST, 1, [24], "Fear of Victory"),
    ("Batman the Animated Series Vol. 1/25. The Clock King.xvid",              DEST, 1, [25], "The Clock King"),
    ("Batman the Animated Series Vol. 1/26. Appointment in Crime Alley.xvid",  DEST, 1, [26], "Appointment in Crime Alley"),
    ("Batman the Animated Series Vol. 1/27. Mad As a Hatter.xvid",             DEST, 1, [27], "Mad as a Hatter"),
    ("Batman the Animated Series Vol. 1/28. Dreams in Darkness.xvid",          DEST, 1, [28], "Dreams in Darkness"),
    # ── Season 1 — Vol. 2 (episodes 29–56) ───────────────────────────────
    ("Batman the Animated Series Vol. 2/29. Eternal Youth.avi",                DEST, 1, [29], "Eternal Youth"),
    ("Batman the Animated Series Vol. 2/30. Perchance To Dream.avi",           DEST, 1, [30], "Perchance to Dream"),
    ("Batman the Animated Series Vol. 2/31. The Cape And Cowl Conspiracy.avi", DEST, 1, [31], "The Cape and Cowl Conspiracy"),
    ("Batman the Animated Series Vol. 2/32. Robin's Reckoning Part One.avi",   DEST, 1, [32], "Robin's Reckoning Part One"),
    ("Batman the Animated Series Vol. 2/33. Robin's Reckoning Part Two.avi",   DEST, 1, [33], "Robin's Reckoning Part Two"),
    ("Batman the Animated Series Vol. 2/34. The Laughing Fish.avi",            DEST, 1, [34], "The Laughing Fish"),
    ("Batman the Animated Series Vol. 2/35. Night Of The Ninja.avi",           DEST, 1, [35], "Night of the Ninja"),
    ("Batman the Animated Series Vol. 2/36. Cat Scratch Fever.avi",            DEST, 1, [36], "Cat Scratch Fever"),
    ("Batman the Animated Series Vol. 2/37. The Strange Secret Of Bruce Wayne.avi", DEST, 1, [37], "The Strange Secret of Bruce Wayne"),
    ("Batman the Animated Series Vol. 2/38. Heart Of Steel Part One.avi",      DEST, 1, [38], "Heart of Steel Part One"),
    ("Batman the Animated Series Vol. 2/39. Heart Of Steel Part Two.avi",      DEST, 1, [39], "Heart of Steel Part Two"),
    ("Batman the Animated Series Vol. 2/40. If You're So Smart, Why Aren't You Rich.avi", DEST, 1, [40], "If You're So Smart, Why Aren't You Rich?"),
    ("Batman the Animated Series Vol. 2/41. Joker's Wild.avi",                 DEST, 1, [41], "Joker's Wild"),
    ("Batman the Animated Series Vol. 2/42. Tyger, Tyger.avi",                 DEST, 1, [42], "Tyger, Tyger"),
    ("Batman the Animated Series Vol. 2/43. Moon Of The Wolf.avi",             DEST, 1, [43], "Moon of the Wolf"),
    ("Batman the Animated Series Vol. 2/44. Day Of The Samurai.avi",           DEST, 1, [44], "Day of the Samurai"),
    ("Batman the Animated Series Vol. 2/45. Terror In The Sky.avi",            DEST, 1, [45], "Terror in the Sky"),
    ("Batman the Animated Series Vol. 2/46. Almost Got 'im.avi",               DEST, 1, [46], "Almost Got 'Im"),
    ("Batman the Animated Series Vol. 2/47. Birds Of A Feather.avi",           DEST, 1, [47], "Birds of a Feather"),
    ("Batman the Animated Series Vol. 2/48. What Is Reality.avi",              DEST, 1, [48], "What Is Reality?"),
    ("Batman the Animated Series Vol. 2/49. I Am The Night.avi",               DEST, 1, [49], "I Am the Night"),
    ("Batman the Animated Series Vol. 2/50. Off Balance.avi",                  DEST, 1, [50], "Off Balance"),
    ("Batman the Animated Series Vol. 2/51. The Man Who Killed Batman.avi",    DEST, 1, [51], "The Man Who Killed Batman"),
    ("Batman the Animated Series Vol. 2/52. Mudslide.avi",                     DEST, 1, [52], "Mudslide"),
    ("Batman the Animated Series Vol. 2/53. Paging The Crime Doctor.avi",      DEST, 1, [53], "Paging the Crime Doctor"),
    ("Batman the Animated Series Vol. 2/54. Zatanna.avi",                      DEST, 1, [54], "Zatanna"),
    ("Batman the Animated Series Vol. 2/55. The Mechanic.avi",                 DEST, 1, [55], "The Mechanic"),
    ("Batman the Animated Series Vol. 2/56. Harley & Ivy.avi",                 DEST, 1, [56], "Harley and Ivy"),
    # ── Season 1 — Vol. 3 (episodes 57–85) ───────────────────────────────
    ("Batman the Animated Series Vol. 3/57. Shadow Of The Bat Part 1.avi",     DEST, 1, [57], "Shadow of the Bat Part 1"),
    ("Batman the Animated Series Vol. 3/58. Shadow Of The Bat Part 2.avi",     DEST, 1, [58], "Shadow of the Bat Part 2"),
    ("Batman the Animated Series Vol. 3/59. Blind as a Bat.avi",               DEST, 1, [59], "Blind as a Bat"),
    ("Batman the Animated Series Vol. 3/60. The Demon's Quest Part 1.avi",     DEST, 1, [60], "The Demon's Quest Part 1"),
    ("Batman the Animated Series Vol. 3/61. The Demon's Quest Part 2.avi",     DEST, 1, [61], "The Demon's Quest Part 2"),
    ("Batman the Animated Series Vol. 3/62. His Silicon Soul.avi",             DEST, 1, [62], "His Silicon Soul"),
    ("Batman the Animated Series Vol. 3/63. Fire From Olympus.avi",            DEST, 1, [63], "Fire From Olympus"),
    ("Batman the Animated Series Vol. 3/64. Read My Lips.avi",                 DEST, 1, [64], "Read My Lips"),
    ("Batman the Animated Series Vol. 3/65. The Worry Men.avi",                DEST, 1, [65], "The Worry Men"),
    ("Batman the Animated Series Vol. 3/66. Sideshow.avi",                     DEST, 1, [66], "Sideshow"),
    ("Batman the Animated Series Vol. 3/67. A Bullet for Bullock.avi",         DEST, 1, [67], "A Bullet for Bullock"),
    ("Batman the Animated Series Vol. 3/68. Trial.avi",                        DEST, 1, [68], "Trial"),
    ("Batman the Animated Series Vol. 3/69. Avatar.avi",                       DEST, 1, [69], "Avatar"),
    ("Batman the Animated Series Vol. 3/70. House & Garden.avi",               DEST, 1, [70], "House and Garden"),
    ("Batman the Animated Series Vol. 3/71. The Terrible Trio.avi",            DEST, 1, [71], "The Terrible Trio"),
    ("Batman the Animated Series Vol. 3/72. Harlequinade.avi",                 DEST, 1, [72], "Harlequinade"),
    ("Batman the Animated Series Vol. 3/73. Time out of Joint.avi",            DEST, 1, [73], "Time Out of Joint"),
    ("Batman the Animated Series Vol. 3/74. Catwalk.avi",                      DEST, 1, [74], "Catwalk"),
    ("Batman the Animated Series Vol. 3/75. Bane.avi",                         DEST, 1, [75], "Bane"),
    ("Batman the Animated Series Vol. 3/76. Baby-Doll.avi",                    DEST, 1, [76], "Baby-Doll"),
    ("Batman the Animated Series Vol. 3/77. The Lion and The Unicorn.avi",     DEST, 1, [77], "The Lion and the Unicorn"),
    ("Batman the Animated Series Vol. 3/78. Showdown.avi",                     DEST, 1, [78], "Showdown"),
    ("Batman the Animated Series Vol. 3/79. Riddlers Reform.avi",              DEST, 1, [79], "Riddler's Reform"),
    ("Batman the Animated Series Vol. 3/80. Second Chance.avi",                DEST, 1, [80], "Second Chance"),
    ("Batman the Animated Series Vol. 3/81. Harley's Holiday.avi",             DEST, 1, [81], "Harley's Holiday"),
    ("Batman the Animated Series Vol. 3/82. Lock-Up.avi",                      DEST, 1, [82], "Lock-Up"),
    ("Batman the Animated Series Vol. 3/83. Make em Laugh.avi",                DEST, 1, [83], "Make 'Em Laugh"),
    ("Batman the Animated Series Vol. 3/84. Deep Freeze.avi",                  DEST, 1, [84], "Deep Freeze"),
    ("Batman the Animated Series Vol. 3/85. Batgirl Returns.avi",              DEST, 1, [85], "Batgirl Returns"),
    # Duplicate MKV copies of 5 Vol. 3 episodes — moved alongside the avi
    # versions so the better copy can be kept after verifying playback.
    ("Batman - The Animated Series - S04E01 - The Terrible Trio.mkv",          DEST, 1, [71], "The Terrible Trio"),
    ("Batman - The Animated Series - S04E02 - Showdown.mkv",                   DEST, 1, [78], "Showdown"),
    ("Batman - The Animated Series - S04E03 - Catwalk.mkv",                    DEST, 1, [74], "Catwalk"),
    ("Batman - The Animated Series - S04E04 - A Bullet for Bullock.mkv",       DEST, 1, [67], "A Bullet for Bullock"),
    ("Batman - The Animated Series - S04E05 - The Lion and the Unicorn.mkv",   DEST, 1, [77], "The Lion and the Unicorn"),
    # ── Season 2 — Vol. 4 / The New Batman Adventures (episodes 1–24) ───��
    ("Batman the Animated Series Vol. 4/86. Holiday Knights.avi",              DEST, 2, [1],  "Holiday Knights"),
    ("Batman the Animated Series Vol. 4/87. Sins Of The Father.avi",           DEST, 2, [2],  "Sins of the Father"),
    ("Batman the Animated Series Vol. 4/88. Cold Comfort.avi",                 DEST, 2, [3],  "Cold Comfort"),
    ("Batman the Animated Series Vol. 4/89. Double Talk.avi",                  DEST, 2, [4],  "Double Talk"),
    ("Batman the Animated Series Vol. 4/90. You Scratch My Back.avi",          DEST, 2, [5],  "You Scratch My Back"),
    ("Batman the Animated Series Vol. 4/91. Never Fear.avi",                   DEST, 2, [6],  "Never Fear"),
    ("Batman the Animated Series Vol. 4/92. Jokers's Millions.avi",            DEST, 2, [7],  "Joker's Millions"),
    ("Batman the Animated Series Vol. 4/93. Growing Pains.avi",                DEST, 2, [8],  "Growing Pains"),
    ("Batman the Animated Series Vol. 4/94. Love Is A Croc.avi",               DEST, 2, [9],  "Love Is a Croc"),
    ("Batman the Animated Series Vol. 4/95. Torch Song.avi",                   DEST, 2, [10], "Torch Song"),
    ("Batman the Animated Series Vol. 4/96. The Ultimate Thrill.avi",          DEST, 2, [11], "The Ultimate Thrill"),
    ("Batman the Animated Series Vol. 4/97. Over The Edge.avi",                DEST, 2, [12], "Over the Edge"),
    ("Batman the Animated Series Vol. 4/98. Mean Seasons.avi",                 DEST, 2, [13], "Mean Seasons"),
    ("Batman the Animated Series Vol. 4/99. Critters.avi",                     DEST, 2, [14], "Critters"),
    ("Batman the Animated Series Vol. 4/100. Cult Of The Cat.avi",             DEST, 2, [15], "Cult of the Cat"),
    ("Batman the Animated Series Vol. 4/101. Animal Act.avi",                  DEST, 2, [16], "Animal Act"),
    ("Batman the Animated Series Vol. 4/102. Old Wounds.avi",                  DEST, 2, [17], "Old Wounds"),
    ("Batman the Animated Series Vol. 4/103. The Demon Within.avi",            DEST, 2, [18], "The Demon Within"),
    ("Batman the Animated Series Vol. 4/104. Legends Of The Dark Knight.avi",  DEST, 2, [19], "Legends of the Dark Knight"),
    ("Batman the Animated Series Vol. 4/105. Girl's Night Out.avi",            DEST, 2, [20], "Girl's Night Out"),
    ("Batman the Animated Series Vol. 4/106. Mad Love.avi",                    DEST, 2, [21], "Mad Love"),
    ("Batman the Animated Series Vol. 4/107. Chemistry.avi",                   DEST, 2, [22], "Chemistry"),
    ("Batman the Animated Series Vol. 4/108. Beware The Creeper.avi",          DEST, 2, [23], "Beware the Creeper"),
    ("Batman the Animated Series Vol. 4/109. Judgement Day.avi",               DEST, 2, [24], "Judgment Day"),
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
    parser = argparse.ArgumentParser(description="Reorganize Batman: The Animated Series files for Plex")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true")
    group.add_argument("--execute", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("organize_batman_animated.log"),
        ],
    )

    moves = build_plan()
    logging.info(f"\nPlan: {len(moves)} file operations")
    moved, skipped, errors = execute_plan(moves, dry_run=not args.execute)
    logging.info(f"\nSummary: moved={moved}  skipped={skipped}  errors={errors}")


if __name__ == "__main__":
    main()
