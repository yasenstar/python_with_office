from docx import Document
doc = Document()

section = doc.sections[0]

# python-docx is using "Letter" size as default

print(section.page_width.cm)

print(section.page_height.mm)