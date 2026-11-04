# Module 5A reference files

These are the instructor and verification files for Module 5A. They are not student material.

There is one folder per station: `station-1` to `station-6`. Each folder holds the complete `app.py` for that station. Stations 2 to 6 also hold a `templates/` folder. Each station is the previous station plus the one idea it teaches. Station 6 is the final app.

## What never changes

The `dataman/` folder and the `tests/` folder never change in any station. The student renames the old `app.py` to `menu.py` and keeps everything else.

## Check the stations

Use a checkout of the M4 template. Run:

    python verify.py <path-to-template-checkout>

Flask and pytest must be installed in the Python you use.

For each station, the script:

1. Copies the template to a temporary folder.
2. Renames `app.py` to `menu.py`.
3. Adds the station's `app.py` and `templates/`.
4. Runs `python -m pytest -q tests`.
5. Calls every route the station has with the Flask test client.

It prints PASS or FAIL for each station. It exits with status 1 if any station fails.

## For students

Write your own code first. Use these files only to compare after you try.
