from docx import Document
import pandas as pd
import re

POS_WORDS = {
    "noun", "verb", "adjective", "adverb",
    "interjection", "phrase", "pronoun",
    "preposition", "conjunction", "numeral",
    "particle", "auxiliary", "idiom"
}

doc = Document("dictionary.docx")
table = doc.tables[0]

rows = []

for row in table.rows[1:]:

    cells = [c.text.strip() for c in row.cells]

    # Remove empty cells
    cells = [c for c in cells if c != ""]

    # Remove consecutive duplicates
    cleaned = []
    for c in cells:
        if not cleaned or cleaned[-1] != c:
            cleaned.append(c)

    if len(cleaned) < 4:
        continue

    # Skip header rows
    if cleaned[0].lower() == "id":
        continue

    if not cleaned[0].isdigit():
        continue

    entry = {
        "id": cleaned[0],
        "khasi": "",
        "english": "",
        "part_of_speech": "",
        "notes": "",
        "page": ""
    }

    # Khasi word is always immediately after the ID
    entry["khasi"] = cleaned[1]

    # Find Part of Speech
    pos_index = -1
    for i, value in enumerate(cleaned):
        if value.lower() in POS_WORDS:
            pos_index = i
            entry["part_of_speech"] = value
            break

    if pos_index == -1:
        continue

    # English is everything between Khasi and POS
    entry["english"] = " ".join(cleaned[2:pos_index]).strip()

    # Notes are after POS (except last page number)
    tail = cleaned[pos_index+1:]

    if tail:
        if tail[-1].isdigit():
            entry["page"] = tail[-1]
            tail = tail[:-1]

        entry["notes"] = " ".join(tail)

    rows.append(entry)

df = pd.DataFrame(rows)

df.to_csv(
    "dataset/master_dictionary.csv",
    index=False,
    encoding="utf-8-sig"
)

print(df.head())
print()
print("Entries:", len(df))
print("Saved.")