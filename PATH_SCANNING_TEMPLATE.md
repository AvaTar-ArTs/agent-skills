# Path Scanning Template

Use this pattern when you are scanning a folder and want temporary output to stay inside the same folder.

## Symbolic Root

- `[ROOT]` = the folder being scanned
- `[ROOT]/tmp` = temporary staging for that scan

## Examples

- `/Users/steven/MySites` -> `[MySites]`
- `/Users/steven/MySites/tmp` -> `[MySites]/tmp`
- `/Users/steven/NotebookLM-AutoMated` -> `[NotebookLM-AutoMated]`
- `/Users/steven/NotebookLM-AutoMated/tmp` -> `[NotebookLM-AutoMated]/tmp`
- `/Users/steven/my-supremepowers` -> `[my-supremepowers]`
- `/Users/steven/my-supremepowers/tmp` -> `[my-supremepowers]/tmp`

## Working Rule

1. Pick the folder you are scanning.
2. Create or use `[ROOT]/tmp` inside that folder.
3. Put scan outputs, scratch files, and transient reports there.
4. Keep durable outputs elsewhere only after review.

## Notes

- If the folder is not writable, say so explicitly.
- Do not silently fall back to a global temp path when the scan root is available.
