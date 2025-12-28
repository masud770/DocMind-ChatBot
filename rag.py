import os
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import RetrievalQA

embeddings = OllamaEmbeddings(model=os.getenv("OLLAMA_EMBEDDING_MODEL", "nomic-embed-text"))
FAISS_PATH = "vectorstore/faiss_index"

def add_document_to_vectorstore(documents, filename: str):
    for i, doc in enumerate(documents):
        doc.metadata.update({
            "source": filename,
            "chunk_id": i,
            "page": doc.metadata.get("page", "N/A"),
            "preview": doc.page_content[:200] + "..." if len(doc.page_content) > 200 else doc.page_content
        })

    vectorstore = FAISS.from_documents(documents, embeddings)

    if os.path.exists(FAISS_PATH):
        existing = FAISS.load_local(FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
        existing.merge_from(vectorstore)
        existing.save_local(FAISS_PATH)
    else:
        vectorstore.save_local(FAISS_PATH)

def get_qa_chain():
    if not os.path.exists(FAISS_PATH):
        return None

    db = FAISS.load_local(FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
    retriever = db.as_retriever(search_kwargs={"k": 8})

    llm = ChatOllama(model=os.getenv("OLLAMA_LLM_MODEL", "llama3.2:3b"), temperature=0.0)

    template = """You are a helpful assistant. Answer using ONLY the provided context.

Rules:
- If the answer is not in the context, say "This information is not found in the document."
- Be concise and accurate.
- Answer in natural English.

Context:
{context}

Question: {question}

Answer:"""

    prompt = PromptTemplate.from_template(template)

    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )