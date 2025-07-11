from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

sample_doc = "/workspaces/RAG-Based-Multi-Agent-Research-Assistant-RA-MARA-/ra-mara/rag/data/sample.txt"

def load_and_split_documents():
    loader = TextLoader(sample_doc)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)
    return chunks
