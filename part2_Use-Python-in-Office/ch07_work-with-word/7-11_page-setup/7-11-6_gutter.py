from docx import Document
from docx.shared import Cm

doc = Document()

section = doc.sections[0]

print(section.gutter.cm)

section.gutter = Cm(1.0)

print(section.gutter.cm)