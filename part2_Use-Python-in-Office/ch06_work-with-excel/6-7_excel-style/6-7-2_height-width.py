from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.row_dimensions[2].height = 50

ws.column_dimensions["C"].width = 50

wb.save("./6-7-2.xlsx")