from PyPDF2 import PdfReader

reader = PdfReader("./9-8-1_2.pdf")

secret = "123456"

if reader.is_encrypted:
    reader.decrypt(secret)

print(reader.pages[2])