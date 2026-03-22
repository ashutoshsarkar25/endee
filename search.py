from sentence_transformers import SentenceTransformer
from endee_client import search_vector

model = SentenceTransformer("all-MiniLM-L6-v2")

query = input("Enter your question: ")
embedding = model.encode(query).tolist()

results = search_vector(embedding)

for i, r in enumerate(results):
    print(f"\nResult {i+1}: {r}")