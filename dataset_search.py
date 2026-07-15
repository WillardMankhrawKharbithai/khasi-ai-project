import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load dataset
df = pd.read_csv("dataset/khasi_dataset.csv")

# User query
query = input("Enter your sentence: ")

# Create embedding for query
query_embedding = model.encode(query, convert_to_tensor=True)

# Store similarity scores
scores = []

# Compare against dataset
for index, row in df.iterrows():

    sentence = row['english']

    sentence_embedding = model.encode(sentence, convert_to_tensor=True)

    similarity = util.cos_sim(query_embedding, sentence_embedding)

    scores.append((sentence, row['khasi'], similarity.item()))

# Sort by similarity
scores = sorted(scores, key=lambda x: x[2], reverse=True)

# Best match
best_match = scores[0]

print("User Query:")
print(query)

print("\nBest Match Found:")
print(best_match[0])

print("\nKhasi Translation:")
print(best_match[1])

print("\nSimilarity Score:")
print(best_match[2])