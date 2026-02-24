def get_prompt(mode: str, user_input: str) -> str:
    if mode == "summarize":
        return f"""
You are a professional analyst.

Summarize the text accurately.

Rules:
- Use only provided text
- No external info

Output:
- 5 bullet points
- Each bullet = 1 sentence

TEXT:
{user_input}
"""

    elif mode == "qa":
        return f"""
You are a cautious assistant.

Answer clearly and concisely.
If unsure, say you are unsure.

QUESTION:
{user_input}

Output:
- One short paragraph
"""

    elif mode == "classify":
        return f"""
You are a strict classifier.

Classify into:
- Positive
- Negative
- Neutral

Return:
Classification: <label>
Reason: <1 sentence>

TEXT:
{user_input}
"""

    elif mode == "rewrite":
        return f"""
You are a professional editor.

Rewrite the text.

Tone: Professional

Rules:
- Keep meaning
- No new info

TEXT:
{user_input}
"""

    elif mode == "plan":
        return f"""
You are a systems planner.

GOAL:
{user_input}

Output:

Steps:
1. ...
2. ...

Assumptions:
- ...

Risks:
- ...
"""

    else:
        return None