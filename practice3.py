import sqlite3

db = sqlite3.connect("practice.db")
db.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, role TEXT, content TEXT)")


def save(role, content):
    db.execute("INSERT INTO messages (role, content) VALUES (?, ?)", (role, content))
    db.commit()


def load():
    rows = db.execute("SELECT role, content FROM messages").fetchall()
    return [{"role": r, "content": c} for r, c in rows]


def clear():
    db.execute("DELETE FROM messages")
    db.commit()


clear()                                  # start fresh
save("user", "My name is Jatin")
save("assistant", "Nice to meet you!")
print(load())
