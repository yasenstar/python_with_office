from docx import Document
doc = Document("./7-6-1_know-run.docx")

paragraph = doc.paragraphs[0]
print(len(paragraph.runs))

for run in paragraph.runs:
    print(run.text)

print(paragraph.runs[4].text)