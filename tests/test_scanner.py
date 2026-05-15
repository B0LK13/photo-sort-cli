"""Unit tests for date extraction logic."""

from datetime import datetime

import pytest

from photo_sort.scanner import (
    get_media_ext,
    is_media_file,
    parse_filename_date,
)


@pytest.mark.parametrize(
    "basename,expected",
    [
        ("photo.jpg", ".jpg"),
        ("photo.jpeg", ".jpeg"),
        ("photo.JPG", ".jpg"),
        ("photo.jpg_", ".jpg_"),
        ("photo.jpeg_", ".jpeg_"),
        ("archive.tar.gz", None),
        ("notes.txt", None),
    ],
)
def test_get_media_ext(basename, expected):
    assert get_media_ext(basename) == expected


@pytest.mark.parametrize(
    "name,expected_date,expected_source",
    [
        ("20190101_035012.jpg", datetime(2019, 1, 1), "filename YYYYMMDD"),
        ("IMG_20200628_1856521.jpg", datetime(2020, 6, 28), "filename YYYYMMDD"),
        ("IMG-20170630-WA0006.jpeg", datetime(2017, 6, 30), "filename YYYYMMDD"),
        ("Screenshot_20190305-071500_Samsung Health.jpg", datetime(2019, 3, 5), "filename YYYYMMDD"),
        ("signal-2018-07-06-115143.jpg", datetime(2018, 7, 6), "filename YYYY-MM-DD"),
        ("Scherm_afbeelding 2024-01-15 om 00.45.02.png", datetime(2024, 1, 15), "filename YYYY-MM-DD"),
        ("20230915_103003000_iOS 18.jpg", datetime(2023, 9, 15), "filename YYYYMMDD"),
        ("Bellen met Richard Baltink-20240120_130303-Opname van vergadering.mp4", datetime(2024, 1, 20), "filename YYYYMMDD"),
        ("random.png", None, None),
    ],
)
def test_parse_filename_date(tmp_path, name, expected_date, expected_source):
    path = tmp_path / name
    path.write_text("")
    date, source = parse_filename_date(str(path))
    assert date == expected_date
    assert source == expected_source
