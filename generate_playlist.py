import argparse
import json
import requests

parser = argparse.ArgumentParser()
parser.add_argument('--year', type=int, choices=range(1984,2011), metavar="[0-100]", required=True)
parser.add_argument('--user_id', type=str, required=True)
parser.add_argument('--token', type=str, required=True)
args = parser.parse_args()

filename_in = "tracks-db-no-duplicates.txt"

###############################################################################
# Create a new playlist...
###############################################################################

token_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + args.token,
}

token_data = {
  "name": "Tracks " + str(args.year),
  "description": "All the tracks from the year.",
}

r = requests.post("https://api.spotify.com/v1/users/" + args.user_id + "/playlists", data=json.dumps(token_data), headers=token_headers)
playlist_id = r.json()["id"]

#for key, value in token_etc.items():
#    print(key, ':\n  ', value)

###############################################################################
# Go through each track from that year...
###############################################################################

nr_added = 0

with open(filename_in) as file:
    for line in file:
        if line[:4] == str(args.year):
            track = line.strip()[16:].split(" - ")
            artist = track[0]
            song = track[1]
            #print(artist, "-", song)

            # Search for artist/song...
            
            user_headers = {
                "Authorization": "Bearer " + args.token,
                "Content-Type": "application/json",
                "Accept": "application/json"
            }

            user_params = {
                "limit": 10,
                #"q": "artist:MO-DO track:EINS, ZWEI, POLIZEI",
                "q": "artist:" + artist + " track:" + song,
                "type": "track"
            }

            #print("artist:" + artist + " track:" + song)

            r = requests.get("https://api.spotify.com/v1/search", params=user_params, headers=user_headers).json()
            #print(r['tracks'].keys())
            if len(r['tracks']['items']) > 0:
                track_uri = r['tracks']['items'][0]['uri']

                # Add track_uri to playlist_id

                token_headers = {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + args.token,
                }

                token_data = {"uris": [track_uri]}

                r = requests.post("https://api.spotify.com/v1/playlists/" + playlist_id + "/tracks", data=json.dumps(token_data), headers=token_headers)
                #token_etc = r.json()

                #for key, value in token_etc.items():
                #    print(key, ':\n  ', value)

                nr_added += 1
            else:
                print("Could not find: " + "artist:" + artist + " track:" + song)

print(str(nr_added) + " tracks added to playlist.")