from openpyxl import load_workbook

wb = load_workbook(filename="./writeonly-test.xlsx", read_only=True)

ws = wb['Sheet']

for row in ws.rows:
    for cell in row:
        print(cell.value)

wb.close()  # do not forget to close() workbook explicitely