from dotenv import load_dotenv
import os
import shutil
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

chroma_db_path = "chroma_db"

if os.path.exists(chroma_db_path):
    shutil.rmtree(chroma_db_path)



# Load environment variables
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
model_name=os.getenv("OPENAI_MODEL")


# Load text file
loader = TextLoader("Relationships.txt", encoding="utf-8")
docs_from_file = loader.load()

# Split the text
text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)
docs = text_splitter.split_documents(docs_from_file)

# Create embedding function
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Set up Chroma DB (you can change the path or persist directory as needed)

db = Chroma(persist_directory=chroma_db_path, embedding_function=embeddings)

# Add documents to Chroma
if not db.get()["documents"]:  # check if DB is empty
    db.add_documents(docs)

retriever = db.as_retriever()

qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name=model_name),
    chain_type="stuff",
    retriever=retriever
)

query = "Which is 5th best batsman?"
response = qa_chain.invoke({"query": query})
print("Response:", response)
