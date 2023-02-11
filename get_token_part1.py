import argparse
from urllib.parse import urlencode

parser = argparse.ArgumentParser()
parser.add_argument('--client_id', type=str, required=True)
args = parser.parse_args()

auth_headers = {
    "client_id": args.client_id,
    "response_type": "code",
    "redirect_uri": "http://localhost:7777/callback",
    "scope": "playlist-modify-public"
}

print("Enter this URL into a web browser:")
print("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))