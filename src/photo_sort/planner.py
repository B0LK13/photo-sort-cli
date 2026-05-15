"""Build a move/copy plan from scanned file information."""

from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import datetime

from photo_sort.scanner import FileInfo


@dataclass(frozen=True, slots=True)
class MoveOp:
    """A single move or copy operation."""

    src: str
    dest: str
    date: datetime
    source: str


def build_plan(
    infos: list[FileInfo],
    root: str,
    *,
    format_template: str = "YYYY/MM",
) -> tuple[list[MoveOp], list[FileInfo]]:
    """Return *(operations, skipped)*.

    *format_template* uses the tokens ``YYYY``, ``MM``, and ``DD``.
    """
    ops: list[MoveOp] = []
    skipped: list[FileInfo] = []

    for info in infos:
        if not info.date:
            skipped.append(info)
            continue

        dest_dir = _apply_template(format_template, root, info.date)
        dest_path = os.path.join(dest_dir, info.basename)
        ops.append(MoveOp(info.path, dest_path, info.date, info.source))

    return ops, skipped


def _apply_template(template: str, root: str, dt: datetime) -> str:
    """Replace tokens in *template* and join with *root*."""
    sub = (
        template.replace("YYYY", str(dt.year))
        .replace("MM", f"{dt.month:02d}")
        .replace("DD", f"{dt.day:02d}")
    )
    return os.path.join(root, sub)
