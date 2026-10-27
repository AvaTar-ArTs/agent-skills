# Suno Catalog ↔ MP3 Reconciliation Notes

Identity rule: ID = identity; duration confirms only; no title matching; ID in filenames; cover rules separate. Commands: `inventory_mp3_covers.py`, `reconcile_suno_catalog.py`, `build_mp3_match_report.py`. Gap pattern: more MP3 files (1507) than CSV unique IDs (663); 249 full UUID + 786 short-hex filename matches; some CSV rows store description text in ID column — filter before identity comparison.
