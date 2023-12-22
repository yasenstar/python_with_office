from PyPDF2 import PdfReader, PdfWriter

watermark_reader = PdfReader("./watermark2.pdf")
watermark_page = watermark_reader.pages[0]

reader = PdfReader("./test1.pdf")

writer = PdfWriter()

for page in reader.pages:    
    watermark_page.merge_page(page)
    writer.add_page(watermark_page)
    watermark_reader = PdfReader("./watermark2.pdf")
    watermark_page = watermark_reader.pages[0]

with open("./9-6_5.pdf", "wb") as f:
    writer.write(f)

# This is the correct result for watermark