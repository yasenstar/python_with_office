import fitz

pdf = fitz.open("./text-3pages.pdf")

page_text_dict = dict()

for index, page in enumerate(pdf.pages()):
    print(f"current is content of page {index}")
    page_text = page.get_text()
    page_text_dict.update({index:page_text})

print(page_text_dict)