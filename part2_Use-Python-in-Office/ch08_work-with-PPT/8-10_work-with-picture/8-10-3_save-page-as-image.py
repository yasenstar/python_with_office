from win32com import client

app = client.Dispatch('PowerPoint.Application')

app.DisplayAlerts = False

ppt = app.Presentations.Open(
    r"D:\GitHub\python_with_office\part2_Use-Python-in-Office\ch08_work-with-PPT\8-10_work-with-picture\8-10-1.pptx",
    WithWindow = False
)

ppt.SaveAs(
    r"D:\GitHub\python_with_office\part2_Use-Python-in-Office\ch08_work-with-PPT\8-10_work-with-picture\8-10-3",
    17
)

ppt.Close()

app.Quit()