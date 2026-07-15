import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load dataset
df = pd.read_csv("dataset/khasi_dataset.csv")

# Store dataset sentences
sentences = df['english'].tolist()

# Generate embeddings ONCE
sentence_embeddings = model.encode(sentences, convert_to_tensor=True)

# User input
query = input("Enter your sentence: ")

# Query embedding
query_embedding = model.encode(query, convert_to_tensor=True)

# Compare query with ALL embeddings at once
similarities = util.cos_sim(query_embedding, sentence_embeddings)

# Get best match index
best_match_index = similarities.argmax().item()

# Retrieve result
best_english = df.iloc[best_match_index]['english']
best_khasi = df.iloc[best_match_index]['khasi']
best_score = similarities[0][best_match_index].item()

# Print results
print("\nBest Match Found:")
print(best_english)

print("\nKhasi Translation:")
print(best_khasi)

print("\nSimilarity Score:")
print(best_score)