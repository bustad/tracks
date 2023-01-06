filename_in = "tracks-db.txt"
filename_out = "tracks-db-no-duplicates.txt"

tracks_db_no_duplicates = []

with open(filename_in) as file:
    for line in file:
        # Append only if the song does not already exist in the list.
        song_exists = False
        for song in tracks_db_no_duplicates:
            if song[16:].lower().strip() == line[16:].lower().strip():
                song_exists = True
        if not song_exists:
            tracks_db_no_duplicates.append(line)
            #print("Adding " + line[16:])

with open(filename_out, 'w') as file:
    for line in tracks_db_no_duplicates:
        file.write(f"{line}")
