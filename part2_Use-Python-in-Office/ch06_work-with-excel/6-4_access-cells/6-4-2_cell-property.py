from openpyxl import Workbook
wb = Workbook()
print(wb.encoding)
ws = wb.active

cell = ws.cell(2,5,"test value")
print(cell.coordinate)
print(cell.value)
print(cell.column_letter)
print(cell.col_idx)
print(cell.row)
print(cell.encoding)