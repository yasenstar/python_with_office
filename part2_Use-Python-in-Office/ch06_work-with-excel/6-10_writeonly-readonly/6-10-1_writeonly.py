from openpyxl import Workbook

from openpyxl.cell import WriteOnlyCell
from openpyxl.comments import Comment
from openpyxl.styles import Font

wb = Workbook(write_only=True)

ws = wb.create_sheet()

for _ in range(100):
    ws.append([i for i in range(200)])
    
cell = WriteOnlyCell(ws, value="Excel")
cell.font = Font(name='黑体', size = 30)
cell.comment = Comment(text="this is comments", author = "yasen")
ws.append([cell])

wb.save("./writeonly-test.xlsx")