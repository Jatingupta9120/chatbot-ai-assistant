from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
MODEL = "llama3.2"

SYSTEM_PROMPT = "You are a friendly, helpful assistant. Keep answers short and clear."
messages = [{"role": "system", "content": SYSTEM_PROMPT}]

print("AI Assistant ready!")
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

    except Exception as e:
        messages.pop()
        print(f"\nError: {e}\n")
