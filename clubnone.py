import sqlite3

plrs_conn = sqlite3.connect("database/Player/plr.db")
club_conn = sqlite3.connect("database/Club/clubs.db")

plrs_cursor = plrs_conn.cursor()
club_cursor = club_conn.cursor()

plrs_cursor.execute('SELECT clubID FROM plrs')
clubIDs = plrs_cursor.fetchall()

for row in clubIDs:
    clubID = 0
    club_cursor.execute('SELECT clubID FROM clubs WHERE clubID=?', (int(clubID),))
    if club_cursor.fetchone() is None:
        plrs_cursor.execute('UPDATE plrs SET clubID=0 WHERE clubID=?', (int(clubID),))
plrs_conn.commit()
club_conn.close()
plrs_conn.close()
