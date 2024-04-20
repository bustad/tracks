import requests
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--urls', type=str, required=True)
parser.add_argument('--tracks', type=str, required=True)
args = parser.parse_args()

urlsfile = args.urls
tracksfile = args.tracks

with open(urlsfile, "r") as fi:
    with open(tracksfile, "w") as fo:
        for line in fi:
            url = line.rstrip()
            if url != "" and url.lstrip()[0] != "#":
                nr = url.split("/")[-1].split("-")[0]
                type = url.split("/")[-2]
                resp = requests.get("https://api.discogs.com/" + type + "s/" + nr)
                jsondict = json.loads(resp.text)
                fo.write("# " + url + "\n")
                for k in range(len(jsondict['tracklist'])):
                    fo.write(jsondict['tracklist'][k]['artists'][0]['name'] + "\t" + jsondict['tracklist'][k]['title'] + "\n")
                fo.write("\n")
