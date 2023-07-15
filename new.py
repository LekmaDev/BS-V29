import sqlite3

try:
    conn = sqlite3.connect('database/Player/plr.db')
    sql = """ALTER TABLE plrs
    ADD buypass INT DEFAULT '0'"""
    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.close()
except sqlite3.Error as e:
    print("end")
finally:
    if (conn):
        conn.close()
        print("done")