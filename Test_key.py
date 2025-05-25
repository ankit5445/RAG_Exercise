# test_openai.py
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    models = openai.models.list()
    print("✅ OpenAI key is valid. Models fetched successfully.")
except Exception as e:
    print("❌ OpenAI key is invalid or there's a connection issue.")
    print(e)
