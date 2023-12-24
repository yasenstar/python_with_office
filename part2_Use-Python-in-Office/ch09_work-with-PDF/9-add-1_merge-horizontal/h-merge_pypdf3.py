from PyPDF3 import PdfFileReader, PdfFileWriter
from PyPDF3.pdf import PageObject

pdf_filenames = ["./test1.pdf", "./test2.pdf"]

input1 = PdfFileReader(open(pdf_filenames[0], "rb"), strict=False)
input2 = PdfFileReader(open(pdf_filenames[1], "rb"), strict=False)

page1 = input1.getPage(0)
page2 = input2.getPage(0)

total_width = page1.mediaBox.upperRight[0] + page2.mediaBox.upperRight[0]
total_height = max([page1.mediaBox.upperRight[1], page2.mediaBox.upperRight[1]])
# print(total_width, total_height)

new_page = PageObject.createBlankPage(None, total_width, total_height)

new_page.mergePage(page1)
new_page.mergeTranslatedPage(page2, page1.mediaBox.upperRight[0], 0)

output = PdfFileWriter()
output.addPage(new_page)
output.write(open("./h-merge_pypdf3.pdf", "wb"))