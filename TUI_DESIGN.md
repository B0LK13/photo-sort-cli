# Photo-Sort TUI Design Document

## Overview

An interactive Text User Interface (TUI) for `photo-sort-cli` that transforms the batch CLI tool into a visual, interactive experience. Users can browse scanned files, preview the sort plan, toggle individual files, adjust settings on-the-fly, and execute with confidence.

**Target framework:** [`textual`](https://textual.textualize.io/) — modern Python TUI framework with reactive UI, CSS-like styling, and excellent widget ecosystem. Added as an optional dependency `[tui]`.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    photo_sort.tui.app                        │
│                     (Textual App)                            │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌─────────────────────────────────────┐  │
│  │  Sidebar     │  │           Main Content Area          │  │
│  │  (Settings)  │  │  (Tabbed: Preview | Log | Summary)   │  │
│  │              │  │                                      │  │
│  │ • Directory  │  │  ┌────────────────────────────────┐  │  │
│  │ • Format     │  │  │      File List (DataTable)      │  │  │
│  │ • Source     │  │  │  ┌────┬──────────┬──────┬─────┐  │  │  │
│  │ • Mode       │  │  │  │ ✅ │ photo... │ 2024 │ exif│  │  │  │
│  │ • Copy/Move  │  │  │  ├────┼──────────┼──────┼─────┤  │  │  │
│  │              │  │  │  │ ⬜ │ video... │ None │ —   │  │  │  │
│  │ [Rescan]     │  │  │  └────┴──────────┴──────┴─────┘  │  │  │
│  │ [Execute]    │  │  │                                  │  │  │
│  │ [Undo]       │  │  │  Status bar: 47 files, 2 skipped │  │  │
│  └──────────────┘  │  └────────────────────────────────┘  │  │
│                    └─────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Module Layout

```
src/photo_sort/
├── __init__.py
├── cli.py              # existing CLI entry point
├── scanner.py          # existing — date extraction
├── planner.py          # existing — plan builder
├── executor.py         # existing — move/copy executor
└── tui/
    ├── __init__.py
    ├── app.py          # Textual App subclass (main loop)
    ├── screens.py      # Screen definitions
    ├── widgets.py      # Custom widgets (FileList, SettingsPanel, etc.)
    ├── themes.py       # Color schemes & styling
    └── bindings.py     # Key binding definitions
```

---

## Screens

### 1. Main Screen (`MainScreen`)

The primary workspace. Split into three zones:

| Zone | Widget | Purpose |
|------|--------|---------|
| Left (25%) | `SettingsPanel` | Configure scan & sort options |
| Center (55%) | `FileDataTable` | Browse, select, preview files |
| Right (20%) | `DetailPane` | Show metadata for selected file |

#### SettingsPanel Widget

Interactive controls bound to reactive state:

```
┌─ Settings ───────────────┐
│ Directory                │
│ [~/Photos/Unsorted    ]  │
│                          │
│ Date Format              │
│ [YYYY/MM ▼]              │
│                          │
│ Source Priority          │
│ [▓▓▓▓] filename         │
│ [▓▓▓░] exif             │
│ [▓▓░░] mtime            │
│                          │
│ [ ] Copy (keep originals)│
│                          │
│ [🔄 Rescan]              │
│                          │
│ [⚡ Execute Sort]        │
│ [↩️  Undo Last]          │
└──────────────────────────┘
```

- **Directory**: Input with `DirectoryTree` picker modal
- **Format**: Dropdown (`YYYY/MM`, `YYYY/MM/DD`, `YYYY`)
- **Source Priority**: Drag-to-reorder list (or ↑/↓ keys)
- **Copy toggle**: Checkbox
- **Rescan**: Re-runs `scan_directory()` + `build_plan()`
- **Execute**: Runs executor (dry-run first, then confirm)
- **Undo**: Reads JSONL log, offers reversal

#### FileDataTable Widget

A `DataTable` showing all files in the selected directory:

```
┌─ Files ─────────────────────────────────────────────┬─ Detail ─┐
│ Sel │ Name              │ Date       │ Source │ Dest │          │
│─────┼───────────────────┼────────────┼────────┼──────┤          │
│ [✓] │ IMG_20240101.jpg  │ 2024-01-01 │ exif   │ 📁   │ Size:    │
│ [✓] │ VID_20240102.mp4  │ 2024-01-02 │ filename│ 📁  │ 12.4 MB  │
│ [ ] │ notes.txt         │ —          │ skip   │ —    │ Type:    │
│ [✓] │ screenshot.png    │ 2024-01-03 │ mtime  │ 📁   │ image/jpeg│
│─────┴───────────────────┴────────────┴────────┴──────┤          │
│ 3 selected  │  1 skipped  │  47 total                │          │
└──────────────────────────────────────────────────────┴──────────┘
```

Columns:
1. **Select** — Checkbox to include/exclude from plan
2. **Name** — Filename (truncated with ellipsis)
3. **Date** — Resolved date or `—`
4. **Source** — `exif`, `filename`, `mtime`, or `skip`
5. **Dest** — Icon showing if destination subfolder exists (`📁` = planned)

Interactions:
- `Space` — Toggle selection of current row
- `Enter` — Open "File Detail" modal
- `a` — Select all
- `n` — Select none
- `i` — Invert selection
- `d` — Toggle detail pane visibility

#### DetailPane Widget

Shows expanded info for the highlighted file:

```
┌─ Detail ─────────────┐
│ IMG_20240101.jpg     │
│                      │
│ 📅 2024-01-01 14:32  │
│ 📍 Source: EXIF      │
│ 📁 Dest: 2024/01/    │
│ 📏 3.2 MB            │
│ 🔧 4032×3024         │
│                      │
│ [Preview] [Exclude]  │
└──────────────────────┘
```

---

### 2. Execute Confirmation Modal (`ExecuteModal`)

When user presses `[Execute]`:

```
┌─ Confirm Execution ──────────────┐
│                                  │
│  Ready to sort 45 files          │
│  Mode: MOVE                      │
│  Format: YYYY/MM                 │
│  Log: photo-sort.log.jsonl       │
│                                  │
│  ⚠️ This will modify your files  │
│                                  │
│  [ Execute for Real ] [Cancel]   │
│  [ Dry Run Only ]                │
│                                  │
└──────────────────────────────────┘
```

Pressing `Enter` on "Execute for Real" requires holding `Shift` or typing "YES" to prevent accidental execution.

---

### 3. Directory Picker Modal (`DirectoryPicker`)

Built-in Textual `DirectoryTree` for selecting the scan root:

```
┌─ Select Directory ───────────────┐
│ /home/user/Photos                │
│ 📁 ..                            │
│ 📁 2023/                         │
│ 📁 Unsorted/   ← highlighted     │
│ 📁 Archive/                      │
│                                  │
│ [Select] [Cancel]                │
└──────────────────────────────────┘
```

---

### 4. Execution Progress Screen (`ProgressScreen`)

Shown during actual execution (not dry-run):

```
┌─ Sorting... ─────────────────────┐
│                                  │
│  Moving files...                 │
│  ████████████████░░░░░░░░  47%   │
│                                  │
│  Current: IMG_2024...jpg         │
│  To: 2024/01/IMG_2024...jpg      │
│                                  │
│  Done: 23  Errors: 0  Skipped: 1 │
│                                  │
│  [ ⛔ Cancel ]                   │
│                                  │
└──────────────────────────────────┘
```

---

### 5. Summary Screen (`SummaryScreen`)

Post-execution report:

```
┌─ Sort Complete ──────────────────┐
│                                  │
│  ✅ 45 files sorted               │
│  ⏭️  2 files skipped              │
│  ❌ 0 errors                      │
│                                  │
│  Log saved to:                   │
│  photo-sort.log.jsonl            │
│                                  │
│  [Open Log] [Back to Main] [Quit]│
│                                  │
└──────────────────────────────────┘
```

---

## Key Bindings (Global)

| Key | Action |
|-----|--------|
| `q` / `Ctrl+C` | Quit (with confirm if unsorted changes pending) |
| `?` / `F1` | Toggle help overlay |
| `r` | Rescan directory |
| `Tab` | Cycle focus (Settings → File List → Detail) |
| `1` / `2` / `3` | Jump to tab: Preview / Log / Summary |

---

## Data Flow

```
User edits setting
       │
       ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Reactive     │────▶│ Re-scan      │────▶│ build_plan() │
│ State (App)  │     │ scan_directory│     │              │
└──────────────┘     └──────────────┘     └──────────────┘
                                                  │
                                                  ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ UI Updates   │◀────│ FileDataTable│◀────│ Plan + Filter│
│ (reactive)   │     │ (reactive)   │     │ (App state)  │
└──────────────┘     └──────────────┘     └──────────────┘
                                                  │
                                   User clicks [Execute]
                                                  │
                                                  ▼
                                          ┌──────────────┐
                                          │ Executor.run()│
                                          │ (dry or real) │
                                          └──────────────┘
```

### Reactive State Model

The `PhotoSortApp` holds a central reactive state:

```python
class PhotoSortApp(App):
    # Reactive state — changes trigger UI updates automatically
    directory: reactive[Path] = reactive(Path.home() / "Pictures")
    format_template: reactive[str] = reactive("YYYY/MM")
    source_priority: reactive[list[str]] = reactive(["filename", "exif", "mtime"])
    copy_mode: reactive[bool] = reactive(False)
    
    # Computed state
    file_infos: reactive[list[FileInfo]] = reactive([])
    move_ops: reactive[list[MoveOp]] = reactive([])
    skipped: reactive[list[FileInfo]] = reactive([])
    selected_paths: reactive[set[str]] = reactive(set())  # unchecked = excluded
```

When any setting changes, `watch_*` methods trigger a re-scan and re-plan, updating the table.

---

## Styling (CSS)

Textual uses CSS-like stylesheets. Proposed `tui.css`:

```css
/* App base */
Screen { align: center middle; }

/* Sidebar */
SettingsPanel {
    width: 25;
    height: 100%;
    border: solid $primary;
    padding: 1 2;
}

/* File table */
FileDataTable {
    width: 1fr;
    height: 100%;
    border: solid $primary-lighten-2;
}

/* Detail pane */
DetailPane {
    width: 20;
    height: 100%;
    border: solid $primary-darken-2;
    padding: 1;
}

/* Status colors */
DataTable .source--exif    { color: $success; }
DataTable .source--filename { color: $warning; }
DataTable .source--mtime   { color: $error; }
DataTable .source--skip    { color: $text-muted; }

/* Selected row highlight */
DataTable .cursor { background: $primary-darken-1; }
```

---

## Integration with Existing Code

The TUI reuses all existing modules without modification:

| TUI Action | Existing Function |
|-----------|-------------------|
| Scan | `scanner.scan_directory()` |
| Plan | `planner.build_plan()` |
| Execute | `executor.Executor.run()` |
| Undo | Parse JSONL log + reverse with `shutil.move()` |

The TUI adds only presentation and interaction layers.

---

## Implementation Phases

### Phase 1: Foundation
- Add `textual` as optional dependency: `pip install photo-sort-cli[tui]`
- Create `src/photo_sort/tui/` package
- Build `app.py` with basic layout (Settings + FileTable)
- Wire `scan_directory()` to populate table

### Phase 2: Interactivity
- Add checkbox selection in file table
- Make settings reactive (edit → rescan)
- Add detail pane
- Implement format template & source priority controls

### Phase 3: Execution
- Execute confirmation modal
- Dry-run vs real execution flow
- Progress screen with live updates
- Summary screen

### Phase 4: Polish
- Undo functionality
- Help overlay
- Keyboard shortcuts
- Themes (dark/light)
- Directory picker modal

---

## Entry Point

New console script in `pyproject.toml`:

```toml
[project.optional-dependencies]
tui = ["textual>=0.50.0"]

[project.scripts]
photo-sort = "photo_sort.cli:main"
photo-sort-tui = "photo_sort.tui.app:main"
```

Usage:
```bash
# Launch TUI
photo-sort-tui

# Launch TUI with initial directory
photo-sort-tui ~/Pictures/Unsorted
```

---

## Accessibility & UX Considerations

1. **Safe by default**: The TUI always starts in "preview mode". Execute requires confirmation.
2. **Batch selection**: Keyboard shortcuts (`a`, `n`, `i`) for selecting many files quickly.
3. **Visual hierarchy**: Color-coded source types (green=EXIF, yellow=filename, red=mtime, gray=skip).
4. **Responsive layout**: Works on 80×24 terminals up to full-screen.
5. **Undo visibility**: Log file path always visible; undo action one key away (`u`).

---

## Future Enhancements

- **Image preview**: ASCII art thumbnail via `rich` or `textual-image`
- **Duplicate detection**: Highlight files with identical hashes
- **Recursive scan**: Toggle for subdirectories
- **Custom filters**: Regex exclude/include patterns in UI
- **Multi-directory**: Queue multiple source directories
