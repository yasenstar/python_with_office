from docx import Document
from docx.enum.section import WD_ORIENTATION

doc = Document()

section = doc.sections[0]

section.orientation = WD_ORIENTATION.LANDSCAPE

width = section.page_width
height = section.page_height

section.page_width = height
section.page_height = width

doc.save("./7-11-4_2.docx")