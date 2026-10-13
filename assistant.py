import sqlite3
from pathlib import Path

from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
MODEL = "llama3.2"

SYSTEM_PROMPT = "You are a friendly, helpful assistant. Keep answers short and clear."

db = sqlite3.connect(Path(__file__).with_name("chat.db"))
db.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, role TEXT, content TEXT)")


def save(role, content):
    db.execute("INSERT INTO messages (role, content) VALUES (?, ?)", (role, content))
    db.commit()


def load():
    rows = db.execute("SELECT role, content FROM messages ORDER BY id").fetchall()
    return [{"role": r, "content": c} for r, c in rows]


def clear():
    db.execute("DELETE FROM messages")
    db.commit()


history = load()
messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history

print("AI Assistant ready!")
if history:
    print(f"Loaded {len(history)} messages from your last chat.")
print("Type 'reset' to clear memory, 'quit' to exit.\n")

while True:
    user_input = input("You: ").strip()

    if not user_input:
        continue
    if user_input.lower() in ("quit", "exit"):
        print("Goodbye!")
        break
    if user_input.lower() == "reset":
        messages = messages[:1]
        clear()
        print("Memory cleared.\n")
        continue

    messages.append({"role": "user", "content": user_input})

    try:
        stream = client.chat.completions.create(
            model=MODEL, messages=messages, stream=True
        )
        print("Assistant: ", end="", flush=True)
        reply = ""
        for chunk in stream:
            piece = chunk.choices[0].delta.content
            if piece:
                print(piece, end="", flush=True)
                reply += piece
        print("\n")
        messages.append({"role": "assistant", "content": reply})
        # Save both sides only after a full reply, so a failed turn leaves no half-saved chat
        save("user", user_input)
        save("assistant", reply)

    except Exception as e:
        messages.pop()
        print(f"\nError: {e}\n")
