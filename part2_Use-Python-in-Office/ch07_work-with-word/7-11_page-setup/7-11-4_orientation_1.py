from docx import Document
from docx.enum.section import WD_ORIENTATION

doc = Document()

section = doc.sections[0]

print(section.orientation)

section.orientation = WD_ORIENTATION.LANDSCAPE

print(section.orientation)

doc.save("./7-11-4_1.docx")