from app.rag_pinecone_multi_query.parent_doc_store import store

from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain.retrievers import ParentDocumentRetriever

from langchain.storage import InMemoryStore
from langchain.text_splitter import RecursiveCharacterTextSplitter

from app.rag_pinecone_multi_query.vector_store import vectorstore

# # Split
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
# all_splits = text_splitter.split_documents(docs)
headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on, strip_headers=False)

# This text splitter is used to create the child documents
child_splitter = RecursiveCharacterTextSplitter(chunk_size=400)

def create_retriever(store):
    retriever = ParentDocumentRetriever(
        vectorstore=vectorstore,
        docstore=store,
        child_splitter=child_splitter,
    )
    return retriever
