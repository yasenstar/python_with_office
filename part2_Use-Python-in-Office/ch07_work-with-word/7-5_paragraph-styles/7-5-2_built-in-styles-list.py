from docx import Document
from docx.enum.style import WD_STYLE_TYPE
doc = Document()

styles = doc.styles
paragraph_styles = [s for s in styles if s.type == WD_STYLE_TYPE.PARAGRAPH]

for style in paragraph_styles:
    print(style.name)