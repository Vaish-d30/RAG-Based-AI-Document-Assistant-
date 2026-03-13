import streamlit as st
from rag_pipeline import enhanced_rag, llm
from retriever import RAGRetriever, rag_retriever

st.set_page_config(page_title="RAG Research Assistant", layout="wide")

st.title("📄 AI Research Paper Assistant")
st.write("Ask questions about the research papers in the knowledge base.")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
query = st.text_input("Ask a question")

if st.button("Ask") and query:
    result = enhanced_rag(query, rag_retriever, llm)
    answer = result["answer"]
    sources = result["sources"]

    # Store history
    st.session_state.chat_history.append((query, answer, sources))

#Display chat history
for q, a, s in reversed(st.session_state.chat_history):
    st.markdown(f"**Question:** {q}")
    st.markdown(f"**Answer:** {a}")
    st.markdown("**Sources:**")
    
    for source in s:
        st.write(source)

        st.markdown("---")
