from PyPDF2 import PdfWriter, PdfReader

reader = PdfReader("./test1.pdf")

writer = PdfWriter()

for page in range(len(reader.pages)):
    page = reader.pages[page]
    writer.add_page(page)

# secret = "Passw0rd"
# writer.encrypt(secret)

writer.encrypt("123456")

with open("./9-8-1_2.pdf", "wb") as f:
    writer.write(f)