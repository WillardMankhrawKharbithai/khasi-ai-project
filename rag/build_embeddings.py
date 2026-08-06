import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer

print("=" * 50)
print("KHASI AI - BUILDING VECTOR DATABASE")
print("=" * 50)

# Load dataset
df = pd.read_csv("dataset/master_dictionary.csv")

print(f"Loaded {len(df)} dictionary entries.")

# Load embedding model
print("\nLoading AI embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create persistent database
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="khasi_dictionary"
)

documents = []
embeddings = []
ids = []
metadatas = []

print("\nGenerating embeddings...")

for index, row in df.iterrows():

    document = f"""
Khasi: {row['khasi']}
English: {row['english']}
Part of Speech: {row['part_of_speech']}
Notes: {row['notes']}
"""

    documents.append(document)

    ids.append(f'{row["id"]}_{index}')

    metadatas.append({
        "khasi": str(row["khasi"]),
        "english": str(row["english"]),
        "part_of_speech": str(row["part_of_speech"])
    })

embeddings = model.encode(
    documents,
    show_progress_bar=True
).tolist()

print("\nSaving vectors into ChromaDB...")

BATCH_SIZE = 5000

for i in range(0, len(ids), BATCH_SIZE):

    collection.add(
        ids=ids[i:i+BATCH_SIZE],
        documents=documents[i:i+BATCH_SIZE],
        embeddings=embeddings[i:i+BATCH_SIZE],
        metadatas=metadatas[i:i+BATCH_SIZE]
    )

    print(f"Saved batch {i//BATCH_SIZE + 1}")

print("\nSUCCESS!")
print(f"Stored {len(ids)} dictionary entries.")
print("\nVector database created successfully!")