# Downloader and playlist creator of songs from Tracks

Some early experiments are found in `tracks.ipynb`.

[Launch notebook on binder.org.](https://mybinder.org/v2/gh/bustad/tracks/main)

1. Run `python3 tracks-downloader.py` to download all the entries into `tracks-db.txt`.
2. Run `python3 tracks-db-remove-duplicates.py` to remove duplicates from `tracks-db.txt` and save the remaining entries to `tracks-db-no-duplicates.txt`.
3. Create an application and get the Client ID and Client Secret codes.
   - Head over to [Spotify’s developer dashboard](https://developer.spotify.com/dashboard/) and create a new application.
   - From the app’s dashboard, click the “Edit Settings” button, and add a Redirect URI to `http://localhost:7777/callback`.
   - Obtain the Client ID and Client Secret codes.
4. Run `python3 get_token_part1.py --client_id xxxx` to get a URL to go to. Go to this URL and copy the new URL that the browser was redirected to.
5. Run `python3 get_token_part2.py --client_id xxxx --client_secret yyyy --new_url http://localhost:7777/callback?code=AQA...` to get the access_token.
6. Do `cp tracks-db-no-duplicates.txt tracks-db-no-duplicates-modified.txt` and make any necessary changes to track titles and artists in the latter. Use `python3 check_entries.py --token xxxx --year 1984` to see which tracks can not be found for a specific year.
7. Run `python3 generate_playlist.py --year 1984 --user_id xxxx --token yyyy` to create a playlist for the chosen year.
8. Check the playlist(s) on [Spotify](https://open.spotify.com/).

Created playlists: [1984](https://open.spotify.com/playlist/47p2AVYdwBiEyLgNeaUryi?si=0d262d47eca743fb)