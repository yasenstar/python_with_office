from PyPDF2 import PdfReader

reader = PdfReader("./9-2-1.pdf")

print(len(reader.pages), type(reader))