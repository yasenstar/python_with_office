from PyPDF2 import PdfReader

reader = PdfReader("./test1.pdf")

for page in reader.pages:
    print(type(page))