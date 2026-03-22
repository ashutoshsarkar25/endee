from sentence_transformers import SentenceTransformer
from pypdf import PdfReader
import os
from endee_client import insert_vector

model = SentenceTransformer("all-MiniLM-L6-v2")

def extract_text(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def chunk_text(text, size=200):
    words = text.split()
    return [" ".join(words[i:i+size]) for i in range(0, len(words), size)]

def ingest(folder="mini-search/data"):
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        text = extract_text(path)
        chunks = chunk_text(text)

        for i, chunk in enumerate(chunks):
            embedding = model.encode(chunk).tolist()

            insert_vector(
                id=f"{file}_{i}",
                embedding=embedding,
                text=chunk,
                source=file
            )

        print(f"Ingested {file}")

if __name__ == "__main__":
    ingest()