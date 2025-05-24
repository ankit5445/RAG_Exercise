#Experimenting how to build a RAG application
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access them
openai_key = os.getenv("OPENAI_API_KEY")
db_password = os.getenv("DB_PASSWORD")

print(f"Loaded API key: {openai_key}")