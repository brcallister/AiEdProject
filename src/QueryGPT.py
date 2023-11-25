import os
from openai import OpenAI

try:
    client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
except KeyError:
    raise Exception("Environment Variable 'OPENAI_API_KEY' not set.")

def query_chatgpt(prompt):
    response = client.chat.completions.create(
    # https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo
    model="gpt-3.5-turbo", # TODO Update to 'gpt4-turbo' for production
    messages=prompt,
    max_tokens=1500,
    # Default is 1.0, higher values are more random. >~1.5 can become nonsense.
    temperature=1.2)
    return [choice.message.content.strip() for choice in response.choices]
