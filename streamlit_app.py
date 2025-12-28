import streamlit as st
import requests

st.set_page_config(page_title="DocMind", page_icon="🚀", layout="centered")

st.title("🚀 DocMind")

st.subheader("Smart Retrieval-Augmented Generation Document Chatbot")

st.markdown("""
**Upload any document and ask intelligent questions**  
Supports: PDF • Images (with OCR) • DOCX • TXT • CSV • JSON • Excel  
Features: Multi-document • Source references • Fully private & local (Ollama powered)
""")

API_URL = "http://localhost:8000"

with st.sidebar:
    st.header("📁 Upload Documents")
    uploaded_files = st.file_uploader(
        "Choose files (PDF, Images, JSON, Excel, DOCX, etc.)",
        type=["pdf", "docx", "txt", "csv", "json", "xlsx", "jpg", "jpeg", "png"],
        accept_multiple_files=True
    )

    if uploaded_files:
        for file in uploaded_files:
            files = {"file": (file.name, file.getvalue(), file.type)}
            with st.spinner(f"Uploading {file.name}..."):
                response = requests.post(f"{API_URL}/upload", files=files)
                if response.ok:
                    st.success(f"✅ {file.name} uploaded!")
                else:
                    st.error(f"❌ Error: {response.json().get('detail', 'Upload failed')}")

# Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "sources" in msg:
            with st.expander("📚 Sources"):
                st.json(msg["sources"])

if prompt := st.chat_input("Ask about your documents..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = requests.post(f"{API_URL}/query", json={"question": prompt})
            if response.ok:
                result = response.json()
                st.markdown(result["answer"])
                if result.get("sources"):
                    with st.expander("📚 Sources"):
                        st.json(result["sources"])
                st.session_state.messages.append({"role": "assistant", "content": result["answer"], "sources": result.get("sources")})
            else:
                st.error("Error: " + response.json().get("detail", "Try again"))