from docx import Document
from docx.shared import Cm

doc = Document()

section = doc.sections[0]

print(section.top_margin.cm)
print(section.bottom_margin.cm)
print(section.left_margin.cm)
print(section.right_margin.cm)

section.top_margin = Cm(2)
section.bottom_margin = Cm(1)
section.left_margin = Cm(1.5)
section.right_margin = Cm(4)

print(section.top_margin.cm)
print(section.bottom_margin.cm)
print(section.left_margin.cm)
print(section.right_margin.cm)

doc.save("./7-11-5.docx")