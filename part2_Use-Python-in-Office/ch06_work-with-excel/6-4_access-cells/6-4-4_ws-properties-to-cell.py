from openpyxl import load_workbook
wb = load_workbook("./test.xlsx")
ws = wb.active

# print(type(ws.rows))

# for cells in ws.rows:
#     print(cells)

# print(type(ws.columns))

# for cells in ws.columns:
#     print(cells)

print(type(ws.values))
for rows in ws.values:
    for value in rows:
        print(value)