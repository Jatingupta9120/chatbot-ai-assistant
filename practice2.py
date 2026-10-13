import sqlite3

db = sqlite3.connect("practice.db")
db.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, role TEXT, content TEXT)")

db.execute("INSERT INTO messages (role, content) VALUES ('user', 'Hi, I am Jatin')")
db.execute("INSERT INTO messages (role, content) VALUES ('assistant', 'Nice to meet you, Jatin!')")
db.commit()

rows = db.execute("SELECT role, content FROM messages").fetchall()
print(rows)

# Turn rows into the same format your chatbot uses
messages = [{"role": r, "content": c} for r, c in rows]
print(messages)
