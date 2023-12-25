from PyPDF2 import PdfReader

reader = PdfReader("./旋转2.pdf")

meta = reader.metadata

print(meta.author)

print(meta.creator)

print(meta.producer)

print(meta.title)

print(meta.subject)

for i in range(len(reader.pages)):
    page = reader.pages[i]
    print(page.mediabox.lower_left, page.mediabox.lower_right, page.mediabox.upper_left, page.mediabox.upper_right)