from docx import Document
doc = Document("./7-6-2.docx")


print(len(doc.paragraphs[0].runs))

