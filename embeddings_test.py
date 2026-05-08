from sentence_transformers import SentenceTransformer
# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')
# Example sentence
sentence = "Hello, how are you?"
# Convert sentence into embedding vector
embedding = model.encode(sentence)
# Print results
print("Sentence:")
print(sentence)

print("\nEmbedding Vector:")
print(embedding)

print("\nVector Length:")
print(len(embedding))