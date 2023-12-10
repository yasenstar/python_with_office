from docx import Document
doc = Document()

table = doc.add_table(5,7)

# ========================
 
row = table.rows[2]

print(type(row))

print(type(row.cells))

print(type(row.table))

print(row._index)

print(row.height)

# ========================

column = table.columns[0]

print(type(column))

print(column.cells)

print(type(column.cells))

print(type(column.table))

print(column._index)

print(column.width)     # question: in book it's "None"