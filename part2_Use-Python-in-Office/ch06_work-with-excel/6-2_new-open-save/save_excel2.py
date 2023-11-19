import os.path
from openpyxl import Workbook
wb = Workbook()
path = "./excel_files"
# file_name = "test622_2.xls"
file_name = "test622_2.xlsx"
file_path = os.path.join(path,file_name)
print(file_path)

if not os.path.exists(path):
    os.makedirs(path)

wb.save(file_path)