import sqlite3
import json
print(f"Select method\n1. Clear account for name\n2. Clear account for trophies\n3. Clear Club\n4. Clear FriendList\n5. Clear Bot-Club\n6. Clear account for Name++")
who=input()
if who == '1':
	print("ok")
	config = open('config.json', 'r')
	content = config.read()
	settings = json.loads(content)
	conn = sqlite3.connect('database/Player/plr.db')
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM plrs")
	rows = cursor.fetchall()
	for row in rows:
		if row[2] in settings['DelName']:
		      cursor.execute("DELETE FROM plrs WHERE lowID=?", (row[1],))
		      print(row[2])
		      conn.commit()
	conn.close()
elif who == '2':
	print("ok")
	config = open('config.json', 'r')
	content = config.read()
	settings = json.loads(content)
	conn = sqlite3.connect('database/Player/plr.db')
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM plrs")
	rows = cursor.fetchall()
	for row in rows:
		if row[3] == 0:
		      cursor.execute("DELETE FROM plrs WHERE lowID=?", (row[1],))
		      print(f"{row[3]}")
		      conn.commit()
	conn.close()
elif who == '3':
	conn = sqlite3.connect("database/Player/plr.db")
	c = conn.cursor()
	c.execute("UPDATE plrs SET quests = ?", ('[]',))
	c.execute("SELECT * FROM plrs")
	conn.commit()
	conn.close()
elif who == '4':
	conn = sqlite3.connect("database/Player/plr.db")
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM plrs')
	rows = cursor.fetchall()
	for row in rows:
		friends_json = []
		cursor.execute('UPDATE plrs SET friends=? WHERE lowID=?', (json.dumps(friends_json), row[1]))
	conn.commit()
	conn.close()
elif who == '5':
	config = open('config.json', 'r')
	content = config.read()
	settings = json.loads(content)
	conn = sqlite3.connect("database/Club/clubs.db")
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM clubs")
	rows = cursor.fetchall()
	for row in rows:
		if len(row[9]) == 28:
			print(f"{len(row[9])}-{row[0]}")
			cursor.execute("DELETE FROM clubs WHERE clubID=?", (row[0],))
			conn.commit()
	conn.close()
elif who == '6':
	config = open('config.json', 'r')
	content = config.read()
	settings = json.loads(content)
	conn = sqlite3.connect('database/Player/plr.db')
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM plrs WHERE name LIKE 'player%'")
	rows = cursor.fetchall()
	for row in rows:
		cursor.execute("DELETE FROM plrs WHERE lowID=?", (row[1],))
		print(row[2])
		conn.commit()
	conn.close()