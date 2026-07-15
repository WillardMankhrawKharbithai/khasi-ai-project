import re
import csv

dataset = []

# Read cleaned text
with open("cleaned_dictionary.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:

    line = line.strip()

    # Detect Khasi-English pairs
    if "-" in line:

        parts = line.split("-", 1)

        if len(parts) == 2:

            khasi = parts[0].strip()
            english = parts[1].strip()

            # Basic cleanup
            khasi = re.sub(r'[^A-Za-z ]', '', khasi)
            english = re.sub(r'[^A-Za-z ,.]', '', english)

            if len(khasi) > 1 and len(english) > 1:
                dataset.append([english, khasi])

# Save CSV
with open("generated_dataset.csv", "w", newline="", encoding="utf-8") as f:

    writer = csv.writer(f)

    writer.writerow(["english", "khasi"])

    writer.writerows(dataset)

print("Dataset generated successfully!")
print("Total entries:", len(dataset))