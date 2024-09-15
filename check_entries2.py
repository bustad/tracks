import argparse
import requests
import json
import re

parser = argparse.ArgumentParser()
parser.add_argument('--token', type=str, required=True)
parser.add_argument('--tracks', type=str, required=True)
args = parser.parse_args()

nr_total = 0
nr_not_found = 0
with open(args.tracks) as file:
    for line in file:
        # Replace ' with space, since there seems to be a bug related to this character.
        track = line.strip().replace("'", " ")
        if track != "" and track[0] != "#":
            s = track.split("\t")
            if len(s) < 2:
                print("Missing tab: " + s)
            artist = s[0]
            artist = re.sub("\(.*\)", "", artist)
            song = s[1]
            
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
