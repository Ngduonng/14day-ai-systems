from openai import OpenAI


def generate_answer(user_text: str) -> str:
    # Use Ollama's OpenAI-compatible API
    client = OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama"  # Required by the client, but ignored by Ollama
    )

    resp = client.chat.completions.create(
        model="llama3",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Be concise and correct."},
            {"role": "user", "content": user_text},
        ],
        temperature=0.2,
        max_tokens=300,
    )
    return resp.choices[0].message.content.strip()
