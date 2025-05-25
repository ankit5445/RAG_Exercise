#Experimenting how to build a RAG application
from dotenv import load_dotenv
import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings   
from langchain_community.vectorstores import DeepLake

# Load environment variables from .env file
load_dotenv()

# Access them
openai_key = os.getenv("OPENAI_API_KEY")

#Load a text file
loader = TextLoader("Relationships.txt", encoding="utf-8")
docs_from_file = loader.load()

# Split the text into smaller chunks
text_splitter = CharacterTextSplitter(chunk_size=200,chunk_overlap=20)
docs = text_splitter.split_documents(docs_from_file)

embeddings = OpenAIEmbeddings(model = "text-embedding-3-small")

my_activeloop_org_id = "ankitaggarwal5445"
my_activeloop_dataset_name = "rag-draft1"
dataset_path = f"hub://{my_activeloop_org_id}/{my_activeloop_dataset_name}"

# Create a DeepLake vector store
db = DeepLake(dataset_path=dataset_path, embedding_function=embeddings)
db.add_documents(docs)

print(db)


