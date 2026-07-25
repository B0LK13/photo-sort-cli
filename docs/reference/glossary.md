# Glossary

- **Date source:** A resolver used to derive a `datetime`: filename, EXIF, or file mtime.
- **Dry run:** Default mode that prints planned operations without copying or moving files; directory side effects require explicit validation (`DEBT-001`).
- **FileInfo:** Immutable record describing one scanned file and its resolved date/source.
- **MoveOp:** Immutable planned source/destination operation.
- **Operation log:** JSON-lines file containing successful real-operation records; currently not an executable undo log.
- **Source priority:** Ordered list of date resolvers selected by `--source`.
