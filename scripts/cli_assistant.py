import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import subprocess
from prompts.prompt_library import get_prompt

OLLAMA_PATH = r"C:\Users\ADMIN\AppData\Local\Programs\Ollama\ollama.exe"
MODEL = "llama3"


def call_llm(prompt: str) -> str:
    try:
        result = subprocess.run(
            [OLLAMA_PATH, "run", MODEL],
            input=prompt,
            text=True,
            capture_output=True,
            encoding="utf-8",     # ✅ FIX Unicode
            errors="ignore",      # ✅ tránh crash ký tự lạ
            timeout=60            # ✅ tránh treo
        )

        if result.returncode != 0:
            return f"❌ Error:\n{result.stderr.strip()}"

        output = result.stdout.strip()

        if not output:
            return "⚠️ Model returned empty response."

        return output

    except subprocess.TimeoutExpired:
        return "⏱️ Timeout: Model took too long to respond."
    except FileNotFoundError:
        return "❌ Ollama not found. Check OLLAMA_PATH."
    except Exception as e:
        return f"❌ Unexpected error: {str(e)}"


def main():
    print("=== CLI AI Assistant (Prompt Library + Ollama) ===")
    print("Modes: qa / summarize / classify / rewrite / plan")
    print("Type 'exit' to quit\n")

    while True:
        mode = input("Mode: ").strip().lower()

        if mode in {"exit", "quit"}:
            print("Goodbye.")
            break

        if mode not in {"qa", "summarize", "classify", "rewrite", "plan"}:
            print("❌ Invalid mode\n")
            continue

        user_input = input("You: ").strip()

        if not user_input:
            print("⚠️ Empty input\n")
            continue

        prompt = get_prompt(mode, user_input)

        if not prompt:
            print("❌ Prompt generation failed\n")
            continue

        print("\n⏳ Thinking...\n")

        response = call_llm(prompt)

        print("Assistant:\n")
        print(response)
        print("\n" + "="*50 + "\n")


if __name__ == "__main__":
    main()