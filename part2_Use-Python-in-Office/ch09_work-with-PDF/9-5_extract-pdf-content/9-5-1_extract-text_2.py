from PyPDF2 import PdfReader

reader = PdfReader("./text-3pages.pdf")

page_text_dict = dict()

for index, page in enumerate(reader.pages):
    print(f"current is content of page {index}")
    page_text = page.extract_text()
    page_text_dict.update({index:page_text})

print(page_text_dict)