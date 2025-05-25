from dotenv import load_dotenv
import os
from langchain_openai import OpenAIEmbeddings

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

embedding_model = OpenAIEmbeddings(
    model="text-embedding-ada-002",
    openai_api_key=api_key
)

embedding = embedding_model.embed_query("Hello world!")
print("✅ Embedding generated. Length:", len(embedding))
