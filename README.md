# Downloader and playlist creator of songs from Tracks

This is a little hobby project about downloading all the tracks from the chart show Trackslistan and creating playlists on Spotify for each year. Some early experiments are found in `tracks.ipynb`. The main process of creating playlists is this:

1. Run `python3 tracks-downloader.py` to download all the entries into `tracks-db.txt`.
2. Run `python3 tracks-db-remove-duplicates.py` to remove duplicates from `tracks-db.txt` and save the remaining entries to `tracks-db-no-duplicates.txt`.
3. Create an application and get the Client ID and Client Secret codes.
   - Head over to [Spotify’s developer dashboard](https://developer.spotify.com/dashboard/) and create a new application.
   - From the app’s dashboard, click the “Edit Settings” button, and add a Redirect URI to `http://localhost:7777/callback`.
   - Obtain the Client ID and Client Secret codes.
4. Run `python3 get_token_part1.py --client_id xxxx` to get a URL to go to. Go to this URL and copy the new URL that the browser was redirected to.
5. Run `python3 get_token_part2.py --client_id xxxx --client_secret yyyy --new_url http://localhost:7777/callback?code=AQA...` to get the access_token.
6. Do `cp tracks-db-no-duplicates.txt tracks-db-no-duplicates-modified.txt` and make any necessary changes to track titles and artists in the latter file. Use `python3 check_entries.py --token xxxx --year 1984` to see which tracks can not be found for a specific year and try to refine the title and artist fields to find the tracks.
7. Run `python3 generate_playlist.py --year 1984 --user_id xxxx --token yyyy` to create a playlist for the chosen year. Check that the actual number of songs added to the playlist is the number reported by the script. Also check that the description is added correctly. If not, run this script again.
8. Check the playlist(s) on [Spotify](https://open.spotify.com/).

Created playlists: 
[1984](https://open.spotify.com/playlist/67pojpAPXQyuJoWcrux7l7?si=789c4d0ff75d4e87), 
[1985](https://open.spotify.com/playlist/3kIzWFkqs9mJLF0rFoaWGC?si=50385ee944e34a5b),
[1986](https://open.spotify.com/playlist/5pgDslSqmqrBc7WbNnZAXT?si=e2d1cec91f974d77),
[1987](https://open.spotify.com/playlist/0tpCSF6NMNqLIP4RtOzUtD?si=300a842bf4884d36),
[1988](https://open.spotify.com/playlist/11Ho0qfPpE5EPlUJLADRbr?si=ca021da263ac48c0),
[1989](https://open.spotify.com/playlist/3LtpewojvCzYAkhYmDiOkb?si=8b7bbb77fc274ad8),
[1990](https://open.spotify.com/playlist/3MtaDfkyOUMn7mnsJPruM3?si=f6fdb56add374183),
[1991](https://open.spotify.com/playlist/4IJDLK5dkBdGsV4tXm5TVf?si=95f50a737e774b19),
[1992](https://open.spotify.com/playlist/6SxEsQ9APgcJpu2X53OTEv?si=15bb650ba091406e),
[1993](https://open.spotify.com/playlist/2sGwsQ38uNd3AbjKpjx5dj?si=fbb4be5230bf46a4),
[1994](https://open.spotify.com/playlist/5XiBjEIQcV0bbBmUHC3fhF?si=f187b8a8defa41ca),
[1995](https://open.spotify.com/playlist/7GwKO47RhIays4UVzzs8Hz?si=2508208b96df427f),
[1996](https://open.spotify.com/playlist/1EhhbvIV5XKUvnii14hcBg?si=0504db68770c4ab9),
[1997](https://open.spotify.com/playlist/2u4wWidtrza84XsmBO2M4j?si=84213881a81e4e6d),
[1998](https://open.spotify.com/playlist/2xhSoiBYsUAbjJ4PkFYYHj?si=fda008dd92df4fff),
[1999](https://open.spotify.com/playlist/5P86GioG3OSjlO3f8Vcp0U?si=7482d1c616b54c39),
[2000](https://open.spotify.com/playlist/4hVHOWNNlwS3A6lDdKNscA?si=e2eb81c8da604cc7),
[2001](https://open.spotify.com/playlist/7CDsEGz5CwUxMHn1dJOQcb?si=3d489a259a074712),
[2002](https://open.spotify.com/playlist/0IWLTdpAwMPbneNhVlq6t5?si=a38f002e2c314b1d),
[2003](https://open.spotify.com/playlist/7ph51Y36kPPGshrqwkAQFO?si=c57f179ee17d48e3),
[2004](https://open.spotify.com/playlist/3f8d6O7MmsZ6NFIlOHbS7Z?si=5R0NagpiQYCzJlV5ewp4Iw)

# Playlist creator of songs from CDs

In addition to create playlists of songs from Trackslistan, playlists can now also be created from CD tracklistnings using the discogs.com website and API. The main process of creating playlists is this:

1. Run `python3 discogs-urls-to-tracks.py --urls discogs-radio-city-hits-urls.txt --tracks discogs-radio-city-hits-tracks.txt` to get tracklistnings from urls.
2. Do `cp discogs-radio-city-hits-tracks.txt discogs-radio-city-hits-tracks-modified.txt` and make any necessary changes to track titles and artists in the latter file. Make sure to not replace any tabs with spaces! Use `python3 check_entries2.py --token xxxx --tracks discogs-radio-city-hits-tracks-modified.txt` to see which tracks can not be found and try to refine the title and artist fields to find the tracks.
3. Run `python3 generate_playlist2.py --user_id xxxx --token yyyy --tracks discogs-radio-city-hits-tracks-modified.txt --playlist "Radio City Hits"` to create a playlist. Check that the actual number of songs added to the playlist is the number reported by the script. Also check that the description is added correctly. If not, run this script again.
4. Check the playlist(s) on [Spotify](https://open.spotify.com/).

Created playlists: 
[Radio City Hits (1-10)](https://open.spotify.com/playlist/1BSz0xq4MCwBanQLFpHX24?si=7da0aab275ac4ae3), 
[Absolute Dance (1-2007)](https://open.spotify.com/playlist/5q6M85D8XqxCaKR5mTFmnl?si=e2a5dd04a54b4489)
