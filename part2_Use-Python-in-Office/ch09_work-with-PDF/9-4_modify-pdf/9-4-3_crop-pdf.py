from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader('./test1.pdf')
writer = PdfWriter()

for page in reader.pages:
    page.mediabox.lower_left = (100, 100)
    page.mediabox.lower_right = (500, 100)
    page.mediabox.upper_right = (500, 600)
    page.mediabox.upper_left = (100, 600)
    writer.add_page(page)

with open("./9-4-3.pdf", "wb") as f:
    writer.write(f)