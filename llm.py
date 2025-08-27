import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("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")
client = OpenAI(api_key=api_key)

def ask_gpt(prompt, system_message="You are a helpful data analyst assistant."):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()