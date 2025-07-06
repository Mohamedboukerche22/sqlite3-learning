import sqlite3

conn = sqlite3.connect("data.db")

cursor  = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS user(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               age INTEGER
               )""")

conn.commit()

conn.close()
