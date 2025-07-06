conn = sqlite3.connect("mydata.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Mohamed", 20))

conn.commit()
conn.close()
