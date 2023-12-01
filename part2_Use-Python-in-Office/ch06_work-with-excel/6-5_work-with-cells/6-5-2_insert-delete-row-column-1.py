from openpyxl import Workbook
wb = Workbook()
ws = wb.active

i = 1
for x in range(1,11):
    for y in range(1,21):
        ws.cell(row=x, column=y, value=i)
        i += 1

ws.insert_cols(5)

ws.insert_rows(2,3)

ws.delete_cols(2,3)

ws.delete_rows(5,3)

wb.save("./insert-row-column-1.xlsx")