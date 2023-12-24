# Purpose:      Merge two PDFs (with same total pages) in side by side horizontally
# Author:       Xiaoqi Zhao
# Version 3:    2023/12/24, support merging of two PDFs with different total pages
# Version 2:    2023/12/24, remove dependency from PageObject
# Version 1:    2023/12/23, initialization

from PyPDF3 import PdfFileReader, PdfFileWriter

pdf_filenames = ["./a1.pdf", "./ps002.pdf"]

reader1 = PdfFileReader(open(pdf_filenames[0], "rb"), strict=False)
reader2 = PdfFileReader(open(pdf_filenames[1], "rb"), strict=False)

writer = PdfFileWriter()

for i in range(max(len(reader1.pages), len(reader2.pages))):

    if i < len(reader1.pages):
        page1 = reader1.getPage(i)

    if i < len(reader2.pages):
        page2 = reader2.getPage(i)

    total_width = page1.mediaBox.upperRight[0] + page2.mediaBox.upperRight[0]
    total_height = max([page1.mediaBox.upperRight[1], page2.mediaBox.upperRight[1]])
    print(total_width, total_height)

    new_page = writer.insertBlankPage(total_width, total_height, i)
    
    if len(reader1.pages) > len(reader2.pages):
        if i >= len(reader2.pages):
            new_page.mergePage(page1)
        else:
            new_page.mergePage(page1)
            new_page.mergeTranslatedPage(page2, page1.mediaBox.upperRight[0], 0)
    else:
        if i >= len(reader1.pages):
            new_page.mergePage(page2)
        else:
            new_page.mergePage(page1)
            new_page.mergeTranslatedPage(page2, page1.mediaBox.upperRight[0], 0)

writer.write(open("./test.pdf", "wb"))