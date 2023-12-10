from docx import Document
doc = Document()

section1  = doc.add_section()

section2  = doc.add_section()

print(len(doc.sections))