from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
MODEL = "llama3.2"

print("Testing Ollama connection...\n")

try:
    # 1. Check which models are installed
    models = [m.id for m in client.models.list().data]
    print("Installed models:", models)

    if not any(MODEL in m for m in models):
        print(f"\nModel '{MODEL}' not found. Run:  ollama pull {MODEL}")
    else:
        # 2. Send one test message
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": "Say hello in one short sentence."}],
        )
        print("\nModel replied:", response.choices[0].message.content)
        print("\nSUCCESS: everything works!")

except Exception as e:
    print("FAILED:", e)
    print("Check that Ollama is running: systemctl status ollama")
