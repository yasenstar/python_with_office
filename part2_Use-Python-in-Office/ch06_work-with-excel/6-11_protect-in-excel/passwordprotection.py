from win32com import client

def encrypt_excel(path, old_pwd, new_pwd, read_only_pwd=""):
    app = client.Dispatch('Excel.Application')
    app.DisplayAlerts = False
    wb = app.Workbooks.Open(path, False, False, None, old_pwd, read_only_pwd)
    wb.SaveAs(path, None, new_pwd, read_only_pwd)
    wb.Close()
    app.Quit()

if __name__ == '__main__':
    file_path = r"D:\GitHub\python_with_office\part2_Use-Python-in-Office\ch06_work-with-excel\6-11_protect-in-excel\test.xlsx"
    encrypt_excel(file_path, "", "") # current test.xlsx has no password
    
    
# if you don't use full path you will get following error:

# File "<COMObject <unknown>>", line 5, in Open
# pywintypes.com_error: (-2147352567, 'Exception occurred.', (0, 'Microsoft Excel', "Sorry, we couldn't find test.xlsx. Is it possible it was moved, renamed or deleted?", 'xlmain11.chm', 0, -2146827284), None)   