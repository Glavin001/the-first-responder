from langchain_community.vectorstores import FAISS
from .embeddings import embeddings

def create_vector_db(documents):
    db = FAISS.from_documents(documents, embeddings)
    return db
