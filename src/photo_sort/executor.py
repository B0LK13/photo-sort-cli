"""Execute (or preview) a move/copy plan."""

from __future__ import annotations

import json
import os
import shutil
from dataclasses import asdict

from photo_sort.planner import MoveOp


class Executor:
    """Run or preview a plan."""

    def __init__(self, *, dry_run: bool = True, copy: bool = False, log_path: str | None = None):
        self.dry_run = dry_run
        self.copy = copy
        self.log_path = log_path
        self.executed: list[dict] = []

    def run(self, ops: list[MoveOp]) -> tuple[int, int]:
        """Execute *ops* and return *(performed, skipped)*."""
        performed = 0
        skipped = 0

        for op in ops:
            basename = os.path.basename(op.src)
            if os.path.exists(op.dest):
                print(f"SKIP: {basename} already exists at {op.dest}")
                skipped += 1
                continue

            os.makedirs(os.path.dirname(op.dest), exist_ok=True)
            if self.dry_run:
                print(f"DRY-RUN: {basename} -> {op.dest}  ({op.date.date()}, {op.source})")
                performed += 1
                continue

            try:
                if self.copy:
                    shutil.copy2(op.src, op.dest)
                    action = "Copied"
                else:
                    shutil.move(op.src, op.dest)
                    action = "Moved"
                print(f"{action}: {basename} -> {op.dest}")
                performed += 1
                self.executed.append({
                    "src": op.src,
                    "dest": op.dest,
                    "date": op.date.isoformat(),
                    "source": op.source,
                    "action": "copy" if self.copy else "move",
                })
            except (OSError, shutil.Error) as exc:
                print(f"ERROR: {basename} — {exc}")
                skipped += 1

        if not self.dry_run and self.log_path and self.executed:
            _append_log(self.log_path, self.executed)

        return performed, skipped


def _append_log(path: str, entries: list[dict]) -> None:
    """Append *entries* to a JSON-lines log file."""
    with open(path, "a", encoding="utf-8") as fh:
        for entry in entries:
            fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
