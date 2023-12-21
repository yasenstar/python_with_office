from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("./test1.pdf")
writer = PdfWriter()

for page in reader.pages:
    page_num = reader.get_page_number(page)
    page = page.rotate(-90) if (page_num + 1) % 2 == 0 else page.rotate(90)
    writer.add_page(page)

with open("./9-4-1_2.pdf", "wb") as f:
    writer.write(f)