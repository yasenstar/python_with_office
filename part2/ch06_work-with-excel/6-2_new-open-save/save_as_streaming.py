from tempfile import NamedTemporaryFile
from openpyxl import Workbook

wb = Workbook()

with NamedTemporaryFile() as tmp:
    wb.save(tmp.name)
    tmp.seek(0)
    stream = tmp.read()
    
# need further investigation