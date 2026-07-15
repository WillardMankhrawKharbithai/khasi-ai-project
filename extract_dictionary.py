import fitz  # PyMuPDF

# Open PDF
pdf = fitz.open("resources/khasi_dictionary.pdf")

all_text = ""

# Extract text from every page
for page in pdf:
    text = page.get_text()
    all_text += text + "\n"

# Save extracted text
with open("dictionary_output.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

print("Dictionary extracted successfully!")
print("Saved as dictionary_output.txt")