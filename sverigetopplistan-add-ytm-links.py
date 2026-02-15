import csv
import urllib.parse

filename_in = "sverigetopplistan-album-all-entries-no-duplicates.csv"
filename_out = "sverigetopplistan-album-all-entries-no-duplicates-ytm.csv"

with open(filename_in, 'r', newline='') as csvfile_in, open(filename_out, 'w', newline='') as csvfile_out:
    csvfile_in_reader = csv.reader(csvfile_in)
    csvfile_out_writer = csv.writer(csvfile_out)

    for row in csvfile_in_reader:
        q = urllib.parse.quote_plus(" ".join(row[3:]))
        link = f"https://music.youtube.com/search?q={q}"
        row.append(link)
        csvfile_out_writer.writerow(row)
