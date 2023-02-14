import argparse
import requests
import json

parser = argparse.ArgumentParser()
parser.add_argument('--year', type=int, choices=range(1984,2011), metavar="[0-100]", required=True)
parser.add_argument('--token', type=str, required=True)
args = parser.parse_args()

filename_in = "tracks-db-no-duplicates-modified.txt"

nr_total = 0
nr_not_found = 0
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

            if len(r['tracks']['items']) == 0:
                print("Could not find: " + "artist:" + artist + " track:" + song)
                nr_not_found += 1

            nr_total += 1

print(str(nr_total) + " tracks in total.")
print(str(nr_not_found) + " tracks not found.")