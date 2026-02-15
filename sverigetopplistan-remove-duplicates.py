import csv

filename_in = "sverigetopplistan-album-all-entries.csv"
filename_out = "sverigetopplistan-album-all-entries-no-duplicates.csv"

with open(filename_in, 'r', newline='') as csvfile_in, open(filename_out, 'w', newline='') as csvfile_out:
    csvfile_in_reader = csv.reader(csvfile_in)
    csvfile_out_writer = csv.writer(csvfile_out)

    songs = []

    for row in csvfile_in_reader:
        song = " - ".join(row[3:]).lower()
        if not song in songs:
            csvfile_out_writer.writerow(row)
            songs.append(song)
