# Purpose:      Merge two PDFs (with same total pages) in side by side horizontally
# Author:       Xiaoqi Zhao
# Version 2:    2023/12/24, remove dependency from PageObject
# Version 1:    2023/12/23, initialization

from PyPDF3 import PdfFileReader, PdfFileWriter

pdf_filenames = ["./a1.pdf", "./b1.pdf"]

reader1 = PdfFileReader(open(pdf_filenames[0], "rb"), strict=False)
reader2 = PdfFileReader(open(pdf_filenames[1], "rb"), strict=False)

writer = PdfFileWriter()

for i in range(len(reader1.pages)):

    page1 = reader1.getPage(i)

    page2 = reader2.getPage(i)

    total_width = page1.mediaBox.upperRight[0] + page2.mediaBox.upperRight[0]
    total_height = max([page1.mediaBox.upperRight[1], page2.mediaBox.upperRight[1]])
    print(total_width, total_height)

    new_page = writer.insertBlankPage(total_width, total_height, i)

    new_page.mergePage(page1)
    new_page.mergeTranslatedPage(page2, page1.mediaBox.upperRight[0], 0)

writer.write(open("./h-a-b.pdf", "wb"))