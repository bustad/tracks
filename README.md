# Downloader and playlist creator of songs from Tracks

Some early experiments are found in `tracks.ipynb`.

[Launch notebook on binder.org.](https://mybinder.org/v2/gh/bustad/tracks/main)

1. Run `pyhton3 tracks-downloader.py` to download all the entries into `tracks-db.txt`.
2. Run `python3 tracks-db-remove-duplicates.py` to remove duplicates from `tracks-db.txt` and save the remaining entries to `tracks-db-no-duplicates.txt`.
3. Create an application and get the Client ID and Client Secret codes.
   - Head over to Spotify’s developer dashboard and create a new application.
   - From the app’s dashboard, click the “Edit Settings” button, and add a Redirect URI to `http://localhost:7777/callback`.
   - Obtain the Client ID and Client Secret codes.