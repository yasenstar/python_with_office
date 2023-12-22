import os.path
from win32com.client import DispatchEx

app = DispatchEx("Excel.Application")

app.Visible = False
app.DisplayAlerts = 0

abs_path = os.path.abspath(__file__)
base_dir = os.path.dirname(abs_path)

file_path = os.path.join(base_dir, "test.xlsx")

save_path = os.path.join(base_dir, "test_excel2pdf.pdf")

wb = app.Workbooks.Open(file_path)
wb.ExportAsFixedFormat(0, save_path)

wb.Close()

app.Quit()