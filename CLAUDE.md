# Website pipeline

The `/website` skill (`SKILL.md`), its template, the shared site tools and the lessons log. Before changing anything here, Read `RULES.md` (the website rules) and `LESSONS-INDEX.md` once per session.

- Tools in `tools/` are the one shared copy every site runs through its stubs. After changing a check, run `python dev/selftest.py` (add `--browser` for browser_qa changes).
- After editing `LESSONS.md`, run `python dev/lessons_index.py`; `selftest.py` fails while the index is out of date.
- Commit every change here with the lesson ID in the message.
