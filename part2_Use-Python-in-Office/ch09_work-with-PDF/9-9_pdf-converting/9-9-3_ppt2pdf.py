import os.path
from win32com.client import DispatchEx

app = DispatchEx("PowerPoint.Application")

app.DisplayAlerts = 0

abs_path = os.path.abspath(__file__)
base_dir = os.path.dirname(abs_path)

file_path = os.path.join(base_dir, "test.pptx")

save_path = os.path.join(base_dir, "test_ppt2pdf.pdf")

ppt = app.Presentations.Open(file_path, WithWindow=False)
ppt.SaveAs(save_path, 32)

ppt.Close()

app.Quit()