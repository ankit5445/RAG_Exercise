from dotenv import load_dotenv
import os
from openai import OpenAI

# Load the .env file
load_dotenv()

# Fetch the API key
api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

# Initialize client
client = OpenAI(api_key=api_key)

# Send prompt to GPT-3.5 or GPT-4
response = client.chat.completions.create(
    model=model,  # or "gpt-4" if you have access
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is RAG in AI?"}
    ],
)

# Print the response
print("\n🤖 Response:\n", response.choices[0].message.content)
