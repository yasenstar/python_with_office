from openpyxl import Workbook
wb = Workbook()
ws = wb.active

i = 1
for x in range(1,11):
    for y in range(1,21):
        ws.cell(row=x, column=y, value = i)
        i += 1

ws.move_range("B1:D3", rows=6, cols=-1, translate=False)

wb.save("./move-cells-1.xlsx")