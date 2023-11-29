from openpyxl import Workbook

wb = Workbook()
ws = wb.active

i = 1
for x in range(1, 21):
    for y in range(1,21):
        ws.cell(x, y, i*i)
        i = i + 1

wb.save("./test.xlsx")