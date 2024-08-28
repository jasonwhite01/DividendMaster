import os
import openai
import argparse

from dotenv import load_dotenv
from pathlib import Path

#load secret things
dotenv_path = Path(".env")
load_dotenv(dotenv_path=dotenv_path)
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

#first part of interaction (prompting) the AI chat engine we are using
def get_system_prompt():
    return """
    You are an AI Dividend Analyst. You are asked to make a 3 sentence or less summary recommendation for income investors given this stock symbol:   
    """


def main():
    parser = argparse.ArgumentParser(description="Analyze dividend fit for income investment using AI")
    parser.add_argument("ticker", help="display stocks' dividend fitness for income investement")
    args = parser.parse_args()

    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    model = "gpt-4o-mini"

    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY is not set")
    
    temperature = 0
    messages = [
        {"role": "user", "content": get_system_prompt() + args.ticker},
    ]

    response = client.chat.completions.create(messages=messages, model=model, temperature=temperature)

    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()