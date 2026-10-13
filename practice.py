import sqlite3

db = sqlite3.connect("practice.db")
db.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT)")
db.execute("INSERT INTO notes (text) VALUES ('second note')")
db.commit()

print(db.execute("SELECT * FROM notes").fetchall())
