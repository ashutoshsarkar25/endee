import streamlit as st
from sentence_transformers import SentenceTransformer
from endee_client import search_vector

st.title("📚 AI Semantic Search (Endee Powered)")

model = SentenceTransformer("all-MiniLM-L6-v2")

query = st.text_input("Enter your question:")

if query:
    embedding = model.encode(query).tolist()
    results = search_vector(embedding)

    st.subheader("Top Results:")
    for i, r in enumerate(results):
        st.write(f"**Result {i+1}:** {r}")