import os
from win32com import client

def xls_to_xlsx(path):
    print("Path: {}".format(path))
    if not os.path.isabs(path):
        print(f"not absolute path")
        return
    if not os.path.exists(path):
        print("sorry, file is not found")
        return
    if os.path.splitext(path)[1] != ".xls":
        print("file type is incorrect, not XLS which is expected")
        return
    app = client.Dispatch('Excel.Application')
    app.DisplayAlerts = False
    work_book = app.Workbooks.Open(path)
    work_book.SaveAs(os.path.splitext(path)[0] + ".xlsx", 51)
    work_book.Close()
    app.Quit()

if __name__ == '__main__':
    file = r"D:\GitHub\python_with_office\part2_Use-Python-in-Office\ch06_work-with-excel\6-12_xls-to-xlsx\test.xls"
    # file = "./test.xls"
    xls_to_xlsx(file)