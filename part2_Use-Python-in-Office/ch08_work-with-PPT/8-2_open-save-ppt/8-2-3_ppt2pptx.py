from win32com import client

app = client.Dispatch('Powerpoint.Application')

app.DisplayAlerts = False

ppt = app.Presentations.Open(r"D:\GitHub\python_with_office\part2_Use-Python-in-Office\ch08_work-with-PPT\8-2_open-save-ppt\8-2-3.ppt", WithWindow=False)

ppt.SaveAs(r"D:\GitHub\python_with_office\part2_Use-Python-in-Office\ch08_work-with-PPT\8-2_open-save-ppt\8-2-3.pptx")

ppt.Close()

app.Quit()