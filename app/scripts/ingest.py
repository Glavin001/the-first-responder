import os

from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Pinecone
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_together import Together

from langchain_experimental.text_splitter import SemanticChunker

from app.rag_pinecone_multi_query.parent_doc_store import store

from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_community.document_loaders import DirectoryLoader

from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain.retrievers import ParentDocumentRetriever

from langchain.storage import InMemoryStore
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
# from langchain_community.vectorstores import Chroma
# from langchain_openai import OpenAIEmbeddings

from app.rag_pinecone_multi_query.vector_store import vectorstore

# loader = DirectoryLoader('./data', glob="**/*.md")
loader = DirectoryLoader('./data', glob="**/*.md", loader_cls=UnstructuredMarkdownLoader)

docs = loader.load()

print(len(docs))

# from ..rag_pinecone_multi_query.embeddings import embeddings
from app.rag_pinecone_multi_query.embeddings import embeddings

if os.environ.get("PINECONE_API_KEY", None) is None:
    raise Exception("Missing `PINECONE_API_KEY` environment variable.")

if os.environ.get("PINECONE_ENVIRONMENT", None) is None:
    raise Exception("Missing `PINECONE_ENVIRONMENT` environment variable.")

PINECONE_INDEX_NAME = os.environ.get("PINECONE_INDEX", "langchain-test")

### Ingest code - you may need to run this the first time
# Load
# from langchain_community.document_loaders import WebBaseLoader
# loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
# data = loader.load()

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
# all_splits = markdown_splitter.split_documents(docs)

# This text splitter is used to create the child documents
child_splitter = RecursiveCharacterTextSplitter(chunk_size=400)

semantic_splitter = SemanticChunker(embeddings)

# The vectorstore to use to index the child chunks
# vectorstore = Chroma(
#     collection_name="full_documents", embedding_function=OpenAIEmbeddings()
# )

# Add to vectorDB
# vectorstore = Pinecone.from_documents(
#     documents=all_splits, embedding=OpenAIEmbeddings(), index_name=PINECONE_INDEX_NAME
# )
# retriever = vectorstore.as_retriever()

# # Set up index with multi query retriever
# vectorstore = Pinecone.from_existing_index(PINECONE_INDEX_NAME, embeddings)

# The storage layer for the parent documents
# store = InMemoryStore()
from app.rag_pinecone_multi_query.parent_doc_store import store
# retriever = ParentDocumentRetriever(
#     vectorstore=vectorstore,
#     docstore=store,
#     child_splitter=child_splitter,
#     # child_splitter=semantic_splitter,
#     # child_splitter=markdown_splitter,
# )

from app.rag_pinecone_multi_query.retriever import create_retriever
retriever = create_retriever(store)

# retriever.add_documents(docs, ids=None)
# Batch into groups of 5
batch_size = 1
for i in range(0, len(docs), batch_size):
    print(i)
    docs_batch = docs[i:i+batch_size]
    retriever.add_documents(docs_batch, ids=None)
    break

# added all
# # Dump the store
# keys = list(store.yield_keys())
# print(keys)
# print(len(keys))
# values = store.mget(keys)
# print(values)

# Write to disk
import pickle

def save_object(obj, filename):
    with open(filename, 'wb') as outp:  # Overwrites any existing file.
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

# save_object(retriever, 'retriever.pkl')
save_object(store, 'store.pkl')
