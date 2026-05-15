"""Command-line interface for photo-sort."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from photo_sort import __version__
from photo_sort.executor import Executor
from photo_sort.planner import build_plan
from photo_sort.scanner import (
    DEFAULT_SOURCES,
    parse_exif_date,
    parse_filename_date,
    parse_mtime_date,
    scan_directory,
)


def _positive_int(value: str) -> int:
    iv = int(value)
    if iv < 0:
        raise argparse.ArgumentTypeError(f"{value} is not a non-negative integer")
    return iv


SOURCE_MAP = {
    "exif": parse_exif_date,
    "filename": parse_filename_date,
    "mtime": parse_mtime_date,
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="photo-sort",
        description="Sort photos and videos into folders by date using EXIF, filenames, or file timestamps.",
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Directory containing unsorted photos (default: current directory)",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Actually move/copy files. Without this flag the tool runs in dry-run mode.",
    )
    parser.add_argument(
        "--copy",
        action="store_true",
        help="Copy files instead of moving them.",
    )
    parser.add_argument(
        "--format",
        default="YYYY/MM",
        help="Output folder structure using YYYY, MM, DD tokens (default: YYYY/MM)",
    )
    parser.add_argument(
        "--source",
        default="filename,exif,mtime",
        help="Comma-separated priority of date sources: exif, filename, mtime (default: filename,exif,mtime)",
    )
    parser.add_argument(
        "--log",
        default="photo-sort.log.jsonl",
        help="Path to a JSON-lines undo log (default: photo-sort.log.jsonl)",
    )
    parser.add_argument(
        "--no-log",
        action="store_true",
        help="Disable the undo log.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    root = Path(args.directory).resolve()
    if not root.is_dir():
        print(f"Error: '{root}' is not a directory.", file=sys.stderr)
        return 2

    # Build source priority list
    sources = []
    for key in args.source.split(","):
        key = key.strip().lower()
        if key not in SOURCE_MAP:
            print(f"Error: unknown source '{key}'. Choose from: {', '.join(SOURCE_MAP)}.", file=sys.stderr)
            return 2
        sources.append(SOURCE_MAP[key])

    print(f"Scanning: {root}")
    print(f"Sources : {', '.join(args.source.split(','))}")
    print(f"Format  : {args.format}")
    print(f"Mode    : {'COPY' if args.copy else 'MOVE'} {'(execute)' if args.execute else '(dry-run)'}")
    print()

    infos = scan_directory(str(root), source_priority=sources)
    ops, skipped = build_plan(infos, str(root), format_template=args.format)

    if not ops:
        print("No media files found to sort.")
        return 0

    print(f"Found {len(ops)} file(s) to sort, {len(skipped)} to skip.")
    print()

    executor = Executor(
        dry_run=not args.execute,
        copy=args.copy,
        log_path=None if args.no_log else args.log,
    )
    performed, errors = executor.run(ops)

    print()
    print("=" * 60)
    print(f"Performed : {performed}")
    print(f"Skipped   : {len(skipped)}")
    print(f"Errors    : {errors}")
    if not args.execute:
        print("\nThis was a dry-run. Add --execute to perform the moves.")
    elif not args.no_log:
        print(f"\nUndo log written to: {args.log}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
