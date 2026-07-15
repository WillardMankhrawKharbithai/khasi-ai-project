import re

# Read extracted dictionary text
with open("dictionary_output.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Remove excessive spaces ONLY
cleaned = re.sub(r'[ \t]+', ' ', text)

# Preserve line breaks
cleaned = re.sub(r'\n+', '\n', cleaned)

# Save cleaned text
with open("cleaned_dictionary.txt", "w", encoding="utf-8") as f:
    f.write(cleaned)

print("Dictionary cleaned successfully!")