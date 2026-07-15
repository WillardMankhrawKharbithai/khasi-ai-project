from sentence_transformers import SentenceTransformer, util

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sentences
sentence1 = "I am hungry"
sentence2 = "I want food"
sentence3 = "The weather is nice"

# Convert into embeddings
embedding1 = model.encode(sentence1, convert_to_tensor=True)
embedding2 = model.encode(sentence2, convert_to_tensor=True)
embedding3 = model.encode(sentence3, convert_to_tensor=True)

# Compare similarity
similarity_1_2 = util.cos_sim(embedding1, embedding2)
similarity_1_3 = util.cos_sim(embedding1, embedding3)

# Print results
print(f"Similarity between '{sentence1}' and '{sentence2}':")
print(similarity_1_2.item())

print("\n")

print(f"Similarity between '{sentence1}' and '{sentence3}':")
print(similarity_1_3.item())