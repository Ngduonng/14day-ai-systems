import os
import time
from dotenv import load_dotenv
from google import genai

def call_llm(client, user_text: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=user_text
    )
    return response.text.strip()

def main():
    load_dotenv()

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise SystemExit("Missing GOOGLE_API_KEY. Put it in a .env file.")

    client = genai.Client(api_key=api_key)

    print("CLI Gemini Assistant (type 'exit' to quit)")

    while True:
        user_text = input("\nYou: ").strip()

        if user_text.lower() in {"exit", "quit"}:
            print("Goodbye.")
            break

        if not user_text:
            print("Please enter a question.")
            continue

        try:
            answer = call_llm(client, user_text)
            print("\nAssistant:", answer)
            time.sleep(3)
        except Exception as e:
            print("\nError:", str(e))

if __name__ == "__main__":
    main()