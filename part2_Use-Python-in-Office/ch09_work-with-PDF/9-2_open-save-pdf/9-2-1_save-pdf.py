from PyPDF2 import PdfWriter

writer = PdfWriter()

writer.add_blank_page(595.28, 841.89)
writer.add_blank_page()

with open("./9-2-1.pdf", "wb") as f:
    writer.write(f)