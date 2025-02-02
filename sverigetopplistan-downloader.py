# https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# apt install python3.10-venv
# python3 -m venv .venv
# source .venv/bin/activate

# python3 -m pip install --upgrade pip
# python3 -m pip install beautifulsoup4
# python3 -m pip install requests

from bs4 import BeautifulSoup
import requests
import csv

url_first = "https://sverigetopplistan.se/chart/41/?dspy=1975&dspp=46"

with open('sverigetopplistan-all-entries.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    target_url = url_first
    year = target_url.split("=")[1].split("&")[0]
    week = target_url.split("=")[2]
    resp = requests.get(target_url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    while len(soup.find_all("a", {"title":"Nästa period"})) > 0:
        print(f"Writing year {year}, week {week}...")

        chart_entries = soup.find_all("li", {"class":"charts-list__item"})
        for k in range(len(chart_entries)):
            artist = chart_entries[k].find_all("p", {"class":"artist"})[0].text.strip()
            title = chart_entries[k].find_all("h2", {"class":"title"})[0].text.strip()
            csvwriter.writerow([year, week, k+1, artist, title])

        target_url = soup.find_all("a", {"title":"Nästa period"})[0]['href']
        year = target_url.split("=")[1].split("&")[0]
        week = target_url.split("=")[2]
        resp = requests.get(target_url)
        soup = BeautifulSoup(resp.text, 'html.parser')
