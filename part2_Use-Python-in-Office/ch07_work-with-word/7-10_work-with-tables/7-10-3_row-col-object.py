from docx import Document
doc = Document()

table = doc.add_table(5,7)

# print(type(table))
# print(type(table.rows))
# print(type(table.columns))

# for row in table.rows:
#     print(type(row))

# for column in table.columns:
#     print(type(column))

print(len(table.rows))
print(len(table.columns))