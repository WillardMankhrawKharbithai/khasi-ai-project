import chromadb
from sentence_transformers import SentenceTransformer

print("=" * 50)
print("KHASI AI SEARCH")
print("=" * 50)

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to database
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_collection("khasi_dictionary")

while True:

    query = input("\nSearch (or 'exit'): ")

    if query.lower() == "exit":
        break

    embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=5
    )

    print("\nTop Matches:\n")

    for i, meta in enumerate(results["metadatas"][0], start=1):
        print("=" * 50)
        print(f"Result #{i}")
        print(f"Khasi          : {meta['khasi']}")
        print(f"English        : {meta['english']}")
        print(f"Part of Speech : {meta['part_of_speech']}")
        print()