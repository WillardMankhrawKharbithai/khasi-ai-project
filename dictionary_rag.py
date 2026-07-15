import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("dataset/generated/generated_dataset.csv")

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Convert English words to embeddings
english_embeddings = model.encode(df['english'].astype(str).tolist())

# User query
query = input("Enter English word: ")

# Encode query
query_embedding = model.encode([query])

# Compare similarity
similarities = cosine_similarity(query_embedding, english_embeddings)

# Best match
best_match_index = similarities.argmax()

best_english = df.iloc[best_match_index]['english']
best_khasi = df.iloc[best_match_index]['khasi']
best_score = similarities[0][best_match_index]

print("\nBest Match:")
print(best_english)

print("\nKhasi Translation:")
print(best_khasi)

print("\nSimilarity Score:")
print(best_score)