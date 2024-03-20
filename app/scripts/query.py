from app.rag_pinecone_multi_query.parent_doc_store import store
from app.rag_pinecone_multi_query.retriever import create_retriever

retriever = create_retriever(store)
# docs = retriever.get_relevant_documents("CVE-2021-22205: Critical GitLab Vulnerability")
docs = retriever.get_relevant_documents("how do I solve a Critical GitLab Vulnerability?")

print(docs)
