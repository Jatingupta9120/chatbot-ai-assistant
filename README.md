# Chatbot AI Assistant

A terminal chatbot that runs **entirely on your own machine**. No API keys, no cloud, no cost: it talks to a local [Ollama](https://ollama.com) model (`llama3.2`) through the OpenAI Python SDK.

I'm **Jatin Gupta**, and I'm learning to build AI products in public. This repo is where that starts: small, working, and growing one commit at a time.

```
AI Assistant ready!
Type 'reset' to clear memory, 'quit' to exit.

You: what is an embedding?
Assistant: A list of numbers that represents the meaning of text, so
similar ideas end up close together.

You: reset
Memory cleared.
```

## What it does

- **Streams replies** token by token, so answers appear as they are generated
- **Remembers the conversation** by sending the full message history on every turn
- **`reset`** wipes the memory, **`quit`** exits
- **Recovers from errors** without corrupting the chat history
- **Runs offline** once the model is downloaded

## Run it

You need Python 3.9+ and [Ollama](https://ollama.com/download).

```bash
git clone https://github.com/Jatingupta9120/chatbot-ai-assistant.git
cd chatbot-ai-assistant

ollama pull llama3.2

python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

python index.py       # checks Ollama is running and the model is installed
python assistant.py   # start chatting
```

## How it works

Ollama exposes an OpenAI-compatible API at `http://localhost:11434/v1`, so the standard `openai` client works by pointing `base_url` at it. The whole chatbot is one loop:

1. Read the user's message and append it to `messages`
2. Send the full `messages` list to the model with `stream=True`
3. Print each chunk as it arrives and collect the reply
4. Append the reply to `messages` so the next turn has context

That's about 40 lines in [`assistant.py`](assistant.py).

## What's in the repo

| File | Purpose |
| --- | --- |
| `assistant.py` | The chatbot |
| `index.py` | Connection test: lists installed models and sends one message |
| `practice.py`, `practice2.py`, `practice3.py` | My SQLite experiments: saving and loading chat messages from a database |

## What I'm building next

The chatbot forgets everything when it closes. The `practice` files are me learning SQLite so I can fix that.

- [ ] Persistent memory: save conversations to SQLite and reload them on start
- [ ] Multiple named chat sessions
- [ ] Choose the model and system prompt from the command line
- [ ] A simple web interface

## What I've learned so far

- How chat models actually "remember": they don't, you resend the history
- Streaming responses and handling partial chunks
- Running open models locally with Ollama
- SQL basics: tables, inserts, parameterised queries

## Get in touch

I'm looking for people to learn from and build with. If you're a founder or engineer and something here caught your eye, message me on [LinkedIn](https://www.linkedin.com/in/jatin-gupta9120/) or open an issue here. Feedback on the code is very welcome.

- LinkedIn: [linkedin.com/in/jatin-gupta9120](https://www.linkedin.com/in/jatin-gupta9120/)
- GitHub: [@Jatingupta9120](https://github.com/Jatingupta9120)
