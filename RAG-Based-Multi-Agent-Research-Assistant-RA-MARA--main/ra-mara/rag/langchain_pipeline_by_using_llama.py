from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
from langchain_community.llms import HuggingFacePipeline
import torch

# model_id="meta-llama/Llama-3.2-3B-Instruct"
model_id = "meta-llama/Llama-3.2-1B" 

def load_rag_pipeline():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local("data/faiss_index", embeddings, allow_dangerous_deserialization=True)

    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype =torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto"
    ).to('cpu')

    pipe=pipeline(
        "text-generation",
        model=model,
        tokenizer =tokenizer,
        max_new_tokens= 200 ,
        do_sample=True,
        temperature=0.7
    )
    llm = HuggingFacePipeline(pipeline=pipe)

    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())
    return qa_chain
