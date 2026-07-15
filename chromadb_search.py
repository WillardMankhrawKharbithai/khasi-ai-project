import chromadb
import pandas as pd
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize ChromaDB client
client = chromadb.Client()

# Create collection
collection = client.create_collection(name="khasi_dataset")

# Load dataset
df = pd.read_csv("dataset/khasi_dataset.csv")

# Add data into ChromaDB
for index, row in df.iterrows():

    english_sentence = row['english']
    khasi_translation = row['khasi']

    embedding = model.encode(english_sentence).tolist()

    collection.add(
        ids=[str(index)],
        embeddings=[embedding],
        documents=[english_sentence],
        metadatas=[{"khasi": khasi_translation}]
    )

# User input
query = input("Enter your sentence: ")

# Convert query into embedding
query_embedding = model.encode(query).tolist()

# Search ChromaDB
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=1
)

# Retrieve results
best_match = results['documents'][0][0]
best_khasi = results['metadatas'][0][0]['khasi']

# Print output
print("\nBest Match Found:")
print(best_match)

print("\nKhasi Translation:")
print(best_khasi)