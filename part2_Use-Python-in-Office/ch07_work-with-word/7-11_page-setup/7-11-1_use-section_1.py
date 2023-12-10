from docx import Document
doc = Document()

print(type(doc))

print(type(doc.sections))

section = doc.sections[0]

print(type(section))