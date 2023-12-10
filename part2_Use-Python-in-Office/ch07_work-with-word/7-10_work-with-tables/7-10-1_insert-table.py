from docx import Document
doc = Document()

table = doc.add_table(3,2)

print(type(table))

doc.save("./7-10-1.docx")