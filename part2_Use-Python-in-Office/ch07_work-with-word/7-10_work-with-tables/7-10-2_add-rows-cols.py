from docx import Document
from docx.shared import Cm
doc = Document()

table = doc.add_table(3,3)

table.add_row()
table.add_row()

table.add_column(width=Cm(3))

doc.save("./7-10-2.docx")