from docx import Document
from docx.shared import Cm, Inches

doc = Document()

table = doc.add_table(3,2, style="Table Grid")

print(table.autofit)

table.autofit = False
print(table.autofit)

for row in table.rows:
    row.height = Cm(3)

table.columns[0].width = Cm(1) # this one is not working

table.style = "Dark List Accent 2"

doc.save("./7-10-8.docx")