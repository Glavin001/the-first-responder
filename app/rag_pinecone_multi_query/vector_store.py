from langchain_community.vectorstores import FAISS
from .embeddings import embeddings
import os

from langchain_community.vectorstores import Pinecone
if os.environ.get("PINECONE_API_KEY", None) is None:
    raise Exception("Missing `PINECONE_API_KEY` environment variable.")

if os.environ.get("PINECONE_ENVIRONMENT", None) is None:
    raise Exception("Missing `PINECONE_ENVIRONMENT` environment variable.")

PINECONE_INDEX_NAME = os.environ.get("PINECONE_INDEX", "langchain-test")

# def create_vector_db(documents):
#     db = FAISS.from_documents(documents, embeddings)
#     return db

# Set up index with multi query retriever
vectorstore = Pinecone.from_existing_index(PINECONE_INDEX_NAME, embeddings)
