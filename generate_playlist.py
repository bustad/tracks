import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--year', type=str, required=True)
args = parser.parse_args()

filename_in = "tracks-db.txt"

with open(filename_in) as file:
    for line in file:
        if line[:4] == args.year:
            track = line.strip()[16:].split(" - ")
            artist = track[0]
            song = track[1]
            print(artist, "-", song)