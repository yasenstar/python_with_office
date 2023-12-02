from openpyxl import Workbook
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
    
# set data range for filtering
ws.auto_filter.ref = "A1:D7"

# choose the column for filtering data (start from index 0)
ws.auto_filter.add_filter_column(1, [39, 51, 30])

wb.save("./test.xlsx")