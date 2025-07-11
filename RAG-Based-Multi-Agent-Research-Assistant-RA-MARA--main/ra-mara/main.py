from rag.langchain_pipeline import load_rag_pipeline

rag = load_rag_pipeline()

while True:
    query = input("Ask: ")
    answer = rag.run(query)
    print("Answer:", answer)
