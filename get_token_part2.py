import argparse
import base64
import requests
import os

parser = argparse.ArgumentParser()
parser.add_argument('--client_id', type=str, required=True)
parser.add_argument('--client_secret', type=str, required=True)
parser.add_argument('--new_url', type=str, required=True)
args = parser.parse_args()

code = args.new_url.split("?code=")[1]

encoded_credentials = base64.b64encode(args.client_id.encode() + b':' + args.client_secret.encode()).decode("utf-8")

token_headers = {
    "Authorization": "Basic " + encoded_credentials,
    "Content-Type": "application/x-www-form-urlencoded"
}

token_data = {
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": "http://localhost:7777/callback"
}

r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)
token_etc = r.json()

for key, value in token_etc.items():
    print(key, ':\n   ', value)