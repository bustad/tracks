# Downloader and playlist creator of songs from Tracks

Some early experiments are found in `tracks.ipynb`.

[Launch notebook on binder.org.](https://mybinder.org/v2/gh/bustad/tracks/main)

1. Run `pyhton3 tracks-downloader.py` to download all the entries into `tracks-db.txt`.
2. Run `python3 tracks-db-remove-duplicates.py` to remove duplicates and save the remaining entries to `tracks-db-no-duplicates.txt`.