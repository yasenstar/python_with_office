from PyPDF2 import PdfReader, PdfWriter

watermark_reader = PdfReader("./watermark.pdf")
watermark_page = watermark_reader.pages[0]

reader = PdfReader("./test1.pdf")

writer = PdfWriter()

for page in reader.pages:
    page.merge_page(watermark_page)
    writer.add_page(page)

with open("./9-6_1.pdf", "wb") as f:
    writer.write(f)