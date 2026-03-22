import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("docs")

def insert_vector(id, embedding, text, source):
    collection.add(
        ids=[id],
        embeddings=[embedding],
        documents=[text],
        metadatas=[{"source": source}]
    )

def search_vector(query_embedding):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )
    return results["documents"][0]