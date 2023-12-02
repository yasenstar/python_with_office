from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference
wb = Workbook()
ws = wb.active

# prepare data
rows = [
    ['月份','桃子','西瓜','龙眼'],
    [1, 38, 28, 29],
    [2, 52, 21, 35],
    [3, 39, 20, 69],
    [4, 51, 29, 41],
    [5, 39, 39, 31],
    [6, 30, 41, 39]
]

for row in rows:
    ws.append(row)

# create a chart
c1 = LineChart()
c1.title = "Fruit Line Chart"
c1.style = 13
c1.x_axis.title = "month"
c1.y_axis.title = "sales volume"

# choose the data range for chart
data = Reference(ws, min_col = 2, min_row = 1, max_col = 4, max_row = 7)
c1.add_data(data, titles_from_data = True)

wb.save("./test.xlsx")