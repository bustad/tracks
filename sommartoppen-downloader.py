import requests
import html
import urllib.parse
import csv

html_text = ""
for year in range(1986, 2007 + 1):
    url = f"https://dflund.se/~fernbom/tracks/sommartoppen/{year}.html"
    resp = requests.get(url)
    html_text += resp.text

with open("sommartoppen-html.txt", 'w') as file:
    file.write(html_text)

entries = []
for line in html.unescape(html_text).splitlines():
    if line.startswith("<li>") and line != """<li><A HREF="./">Tillbaka till Sommartoppen</A>""":
        entries.append(line[4:].split("<b>")[0].split("<i>")[0].strip())

# Remove duplicates while preserving the original order. 
# https://www.geeksforgeeks.org/python/python-list-remove-duplicates-and-keep-the-order/
entries = list(dict.fromkeys(entries))

with open("sommartoppen-entries.txt", 'w') as file:
    file.write("\n".join(entries))

with open("sommartoppen-entries-ytm.csv", 'w', newline='') as csvfile_out:
    csvfile_out_writer = csv.writer(csvfile_out)
    for entry in entries:
        q = urllib.parse.quote_plus(entry.replace(" - ", " "))
        link = f"https://music.youtube.com/search?q={q}"
        csvfile_out_writer.writerow(entry.split(" - ") + [link])
