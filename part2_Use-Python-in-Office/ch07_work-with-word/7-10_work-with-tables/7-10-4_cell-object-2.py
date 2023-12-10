from docx import Document
doc = Document()

table = doc.add_table(3,2)

print("traverse by rows")
for row in table.rows:
    for cell in row.cells:
        print(row._index, type(cell))

print("traverse by columns")
for column in table.columns:
    for cell in column.cells:
        print(column._index, type(cell))