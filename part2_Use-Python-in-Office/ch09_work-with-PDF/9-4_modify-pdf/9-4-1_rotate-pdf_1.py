from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("./test1.pdf")
writer = PdfWriter()

for i in range(len(reader.pages)):
    if (i + 1) % 2 == 0:
        page = reader.pages[i].rotate(90)
    else:
        page = reader.pages[i].rotate(-90)
    writer.add_page(page)

with open("./9-4-1_1.pdf", "wb") as f:
    writer.write(f)