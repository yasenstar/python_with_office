from PyPDF2 import PdfWriter

writer = PdfWriter()

writer.add_blank_page(595.28, 841.89)

# secret = "Passw0rd"
# writer.encrypt(secret)

writer.encrypt("123456")

with open("./9-8-1_1.pdf", "wb") as f:
    writer.write(f)