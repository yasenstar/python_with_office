from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("./test1.pdf")
writer = PdfWriter()

page = reader.pages[0]

writer.add_page(page)

print(page.mediabox)
# store dimension as Left, Bottom, Right, Top

print(page.mediabox[3])

print(page.mediabox.left)
print(page.mediabox.bottom)
print(page.mediabox.right)
print(page.mediabox.top)

page.mediabox.right = 300

print(page.mediabox)

writer.add_page(page)

with open("./9-4-2_1.pdf", "wb") as f:
    writer.write(f)