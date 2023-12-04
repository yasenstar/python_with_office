from docx import Document
from docx.shared import Pt

doc = Document()

paragraph = doc.add_paragraph("某一天，Office遇上了Python")

font_size = paragraph.style.font.size

if font_size is None:
    font_size = Pt(10.5)

paragraph.paragraph_format.first_line_indent = font_size * 2

doc.save("./7-7-3.docx")