from docx import Document
from docx.shared import Pt

doc = Document("./test_chinese.docx")

paragraph = doc.paragraphs[1]

font_size = paragraph.style.font.size

print(font_size)

if font_size is None:
    font_size = Pt(10.5)

