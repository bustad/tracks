import argparse
import json
import requests

parser = argparse.ArgumentParser()
parser.add_argument('--year', type=int, choices=range(1984,2011), metavar="[0-100]", required=True)
parser.add_argument('--user_id', type=str, required=True)
parser.add_argument('--token', type=str, required=True)
args = parser.parse_args()

filename_in = "tracks-db-no-duplicates-modified.txt"

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

nr_added = 0
not_found = ""

with open(filename_in) as file:
    for line in file:
        if line[:4] == str(args.year):
            # Replace ' with space, since there seems to be a bug related to this character.
            track = line.strip()[16:].replace("'", " ").split(" - ")
            artist = track[0]
            song = track[1]
            
            user_headers = {
                "Authorization": "Bearer " + args.token,
                "Content-Type": "application/json",
                "Accept": "application/json"
            }

            user_params = {
                "limit": 10,
                "q": "artist:" + artist + " track:" + song,
                "type": "track"
            }

            r = requests.get("https://api.spotify.com/v1/search", params=user_params, headers=user_headers).json()

            if len(r['tracks']['items']) > 0:
                track_uri = r['tracks']['items'][0]['uri']

                token_headers = {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + args.token,
                }

                token_data = {"uris": [track_uri]}

                r = requests.post("https://api.spotify.com/v1/playlists/" + playlist_id + "/tracks", data=json.dumps(token_data), headers=token_headers)

                nr_added += 1
            else:
                print("Could not find: " + "artist:" + artist + " track:" + song)
                if not_found == "":
                    not_found = "Tracks not found: "
                else:
                    not_found += ", "
                not_found = not_found + artist + " - " + song

print(str(nr_added) + " tracks added to playlist.")

if not_found != "":
    token_headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + args.token,
    }


    token_data = {
        "name": "Tracks " + str(args.year),
        "description": not_found,
    }

    r = requests.put("https://api.spotify.com/v1/playlists/" + playlist_id, data=json.dumps(token_data), headers=token_headers)