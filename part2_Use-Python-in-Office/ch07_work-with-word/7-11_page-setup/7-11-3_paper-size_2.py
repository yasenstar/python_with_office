from docx import Document
from docx.shared import Cm

doc = Document()

section = doc.sections[0]

# python-docx is using "Letter" size as default

print(section.page_width.cm)

print(section.page_height.mm)

# set Page size to A4

section.page_width = Cm(21.0)
section.page_height = Cm(29.7)

print(section.page_width.cm)

print(section.page_height.mm)

# set Page size to Legal

section.page_width = Cm(21.59)
section.page_height = Cm(35.56)

print(section.page_width.cm)

print(section.page_height.mm)

# set Page size to non-standard

section.page_width = Cm(11.59)
section.page_height = Cm(25.56)

print(section.page_width.cm)

print(section.page_height.mm)


doc.save("./7-11-3_2.docx")