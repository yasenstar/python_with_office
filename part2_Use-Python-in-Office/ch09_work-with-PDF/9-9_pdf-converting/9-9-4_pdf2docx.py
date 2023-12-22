from pdf2docx import Converter

converter = Converter("./TSLA-Q3-2023-Update-3.pdf")

converter.convert("./Tesla.docx")

converter.close()