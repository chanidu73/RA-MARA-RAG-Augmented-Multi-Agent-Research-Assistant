from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from rag.load_docs import load_and_split_documents

def create_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    docs = load_and_split_documents()
    faiss_index = FAISS.from_documents(docs, embeddings)
    faiss_index.save_local("data/faiss_index")
