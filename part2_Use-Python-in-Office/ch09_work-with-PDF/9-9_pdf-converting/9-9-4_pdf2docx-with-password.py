from pdf2docx import Converter

converter = Converter("./9-8-1_2.pdf", password = "123456")

converter.convert("./9-9-4_with-password.docx")

converter.close()