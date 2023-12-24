# Purpose:      Merge two PDFs (with same total pages) in side by side horizontally
# Author:       Xiaoqi Zhao
# Version 1:    2023/12/23, initialization

from PyPDF3 import PdfFileReader, PdfFileWriter
from PyPDF3.pdf import PageObject

pdf_filenames = ["./test1.pdf", "./test2.pdf"]

reader1 = PdfFileReader(open(pdf_filenames[0], "rb"), strict=False)
reader2 = PdfFileReader(open(pdf_filenames[1], "rb"), strict=False)

writer = PdfFileWriter()

page1 = reader1.getPage(0)
page2 = reader2.getPage(0)

for i in range(len(reader1.pages)):

    page1 = reader1.getPage(i)
    page2 = reader2.getPage(i)

    total_width = page1.mediaBox.upperRight[0] + page2.mediaBox.upperRight[0]
    total_height = max([page1.mediaBox.upperRight[1], page2.mediaBox.upperRight[1]])
    # print(total_width, total_height)

    new_page = writer.insertBlankPage(total_width, total_height, i)

    new_page.mergePage(page1)
    new_page.mergeTranslatedPage(page2, page1.mediaBox.upperRight[0], 0)

    # writer.addPage(new_page)

writer.write(open("./h-merge_pypdf3-multipage.pdf", "wb"))