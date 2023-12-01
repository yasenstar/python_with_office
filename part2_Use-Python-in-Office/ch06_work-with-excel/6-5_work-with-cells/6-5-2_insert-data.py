from openpyxl import Workbook
wb = Workbook()
ws = wb.active

ws.append(["序号","最高温度","最低温度"])
ws.append([1, 32, 15])
ws.append([2, 15, 12])

for i in range(3, 20):
    ws.append([i, i*5, i*2])

wb.save("./insert-data.xlsx")