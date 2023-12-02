from openpyxl import Workbook
wb = Workbook()
ws = wb.active

ws.protection.password = "456"
ws.protection.sheet = True

wb.save("./6-11-2.xlsx")