"""Date extraction from EXIF, filenames, and file system metadata."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from datetime import datetime
from typing import Callable

from PIL import Image
from PIL.ExifTags import TAGS

MEDIA_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".tiff",
    ".webp",
    ".heic",
    ".mp4",
    ".mov",
    ".avi",
    ".mkv",
    ".wmv",
    ".flv",
    ".mpeg",
    ".mpg",
    ".3gp",
    ".jpg_",
    ".jpeg_",
}

EXIF_DATE_TAGS = [
    (36867, "DateTimeOriginal"),  # 0x9003
    (36868, "DateTimeDigitized"),  # 0x9004
    (306, "DateTime"),  # 0x0132
]

FILENAME_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    # 20190101_035012 or IMG_20190101_035012 or 20230915_103003000
    (re.compile(r"(\d{4})(\d{2})(\d{2})[_\-]\d{6}"), "YYYYMMDD"),
    # WhatsApp: IMG-20170630-WA0006, VID-20190312-WA0001
    (re.compile(r"[A-Z]{2,4}-(\d{4})(\d{2})(\d{2})-WA\d+"), "YYYYMMDD"),
    # Screenshot_20190305-071500, signal-2018-07-06-115143
    (re.compile(r"(\d{4})[\-_](\d{2})[\-_](\d{2})"), "YYYY-MM-DD"),
    # Scherm_afbeelding 2024-01-15 om 00.45.02
    (re.compile(r"(\d{4})-(\d{2})-(\d{2})"), "YYYY-MM-DD"),
]


def get_media_ext(basename: str) -> str | None:
    """Return the recognised media extension for *basename*, or *None*."""
    b = basename.lower()
    for ext in sorted(MEDIA_EXTENSIONS, key=len, reverse=True):
        if b.endswith(ext):
            return ext
    return None


def is_media_file(filepath: str) -> bool:
    """Return *True* if *filepath* looks like a media file."""
    return get_media_ext(os.path.basename(filepath)) is not None


def parse_exif_date(filepath: str) -> tuple[datetime, str] | tuple[None, None]:
    """Try to read a date from the image's EXIF data."""
    try:
        img = Image.open(filepath)
    except Exception:
        return None, None

    exif = img._getexif()
    if not exif:
        return None, None

    for tag_id, tag_name in EXIF_DATE_TAGS:
        raw = exif.get(tag_id)
        if not raw:
            continue
        try:
            dt = datetime.strptime(raw, "%Y:%m:%d %H:%M:%S")
            return dt, f"EXIF {tag_name}"
        except ValueError:
            continue

    return None, None


def parse_filename_date(filepath: str) -> tuple[datetime, str] | tuple[None, None]:
    """Try to extract a date from the file name."""
    basename = os.path.basename(filepath)
    for pattern, label in FILENAME_PATTERNS:
        match = pattern.search(basename)
        if not match:
            continue
        try:
            year, month, day = int(match.group(1)), int(match.group(2)), int(match.group(3))
            if 1990 <= year <= 2100 and 1 <= month <= 12 and 1 <= day <= 31:
                return datetime(year, month, day), f"filename {label}"
        except ValueError:
            continue
    return None, None


def parse_mtime_date(filepath: str) -> tuple[datetime, str] | tuple[None, None]:
    """Fall back to the file's modification time."""
    try:
        mtime = os.path.getmtime(filepath)
        return datetime.fromtimestamp(mtime), "file mtime"
    except (OSError, ValueError):
        return None, None


# Default priority order for date sources.
DEFAULT_SOURCES: list[Callable[[str], tuple[datetime, str] | tuple[None, None]]] = [
    parse_filename_date,
    parse_exif_date,
    parse_mtime_date,
]


@dataclass(frozen=True, slots=True)
class FileInfo:
    """Result of scanning a single file."""

    path: str
    basename: str
    date: datetime | None
    source: str
    is_media: bool


def scan_directory(
    root: str,
    *,
    source_priority: list[Callable[[str], tuple[datetime, str] | tuple[None, None]]] | None = None,
) -> list[FileInfo]:
    """Return a *FileInfo* for every file in *root* (non-recursive)."""
    sources = source_priority or DEFAULT_SOURCES
    results: list[FileInfo] = []

    for name in sorted(os.listdir(root)):
        path = os.path.join(root, name)
        if not os.path.isfile(path):
            continue

        if not is_media_file(path):
            results.append(FileInfo(path, name, None, "skipped (not media)", False))
            continue

        date: datetime | None = None
        source_str = "no date found"
        for source in sources:
            dt, src_label = source(path)
            if dt:
                date = dt
                source_str = src_label
                break

        results.append(FileInfo(path, name, date, source_str, True))

    return results
