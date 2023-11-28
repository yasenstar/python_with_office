from openpyxl import Workbook
wb = Workbook()
# ws = wb.active()
ws = wb.active
print(type(ws), ws)