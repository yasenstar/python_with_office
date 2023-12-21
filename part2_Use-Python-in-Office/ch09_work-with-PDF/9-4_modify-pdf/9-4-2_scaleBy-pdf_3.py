from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("./test1.pdf")
writer = PdfWriter()

for page in reader.pages:
    page.scale_by(0.1)
    writer.add_page(page)

with open("./9-4-2_3.pdf", "wb") as f:
    writer.write(f)