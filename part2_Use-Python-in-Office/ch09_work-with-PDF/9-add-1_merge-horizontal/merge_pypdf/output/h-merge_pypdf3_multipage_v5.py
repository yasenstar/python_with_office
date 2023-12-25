# Purpose:      Merge two PDFs (with same total pages) in side by side horizontally
# Author:       Xiaoqi Zhao
# Version 5:    2023/12/25, WIP, research on how to cropped content can be applied to the source PDF
# Version 4:    2023/12/24, implement page both in middle of vertical direction
# Version 3:    2023/12/24, support merging of two PDFs with different total pages
# Version 2:    2023/12/24, remove dependency from PageObject
# Version 1:    2023/12/23, initialization

from PyPDF3 import PdfFileReader, PdfFileWriter
from PyPDF3.generic import RectangleObject

pdf_sources = ["./1.pdf", "./2.pdf"]

reader1_origin = PdfFileReader(open(pdf_sources[0], "rb"), strict=False)
reader2_origin = PdfFileReader(open(pdf_sources[1], "rb"), strict=False)

writer1 = PdfFileWriter()
writer2 = PdfFileWriter()

for i in range(len(reader1_origin.pages)):
    page1_origin = reader1_origin.pages[i]
    page1_origin.mediaBox.upper_left= (58, 570)
    page1_origin.mediaBox.upper_right= (760, 570)
    page1_origin.mediaBox.lower_left= (58, 80)
    page1_origin.mediaBox.lower_right= (760, 80)
    page1_origin.cropBox.upper_left= (58, 570)
    page1_origin.cropBox.upper_right= (760, 570)
    page1_origin.cropBox.lower_left= (58, 80)
    page1_origin.cropBox.lower_right= (760, 80)
    page1_origin.update({'/CropBox': RectangleObject([58, 80, 760, 570])})
    page1_origin.update({'/MediaBox': RectangleObject([58, 80, 760, 570])})
    writer1.addPage(page1_origin)
    
for i in range(len(reader2_origin.pages)):
    page2_origin = reader2_origin.pages[i]
    # page2_origin.update({'/CropBox': RectangleObject([58, 80, 760, 570])})
    # page2_origin.update({'/MediaBox': RectangleObject([58, 80, 760, 570])})
    writer2.addPage(page2_origin)

writer1.write(open("./1-new.pdf", "wb"))
writer2.write(open("./2-new.pdf", "wb"))

pdf_filenames = ["./1-new.pdf", "./2-new.pdf"]

reader1 = PdfFileReader(open(pdf_filenames[0], "rb"), strict=False)
reader2 = PdfFileReader(open(pdf_filenames[1], "rb"), strict=False)

file1_width = reader1.getPage(0).mediaBox.upperRight[0]

writer = PdfFileWriter()

for i in range(max(len(reader1.pages), len(reader2.pages))):

    if i < len(reader1.pages):
        page1 = reader1.getPage(i)

    if i < len(reader2.pages):
        page2 = reader2.getPage(i)

    print(page1.mediaBox, page2.mediaBox)

    total_width = page1.mediaBox.upperRight[0] + page2.mediaBox.upperRight[0]
    total_height = max([page1.mediaBox.upperRight[1], page2.mediaBox.upperRight[1]])
    print(total_width, total_height)

    new_page = writer.insertBlankPage(total_width, total_height, i)
    
    print(page1.mediaBox, page2.mediaBox)
    print(page1.cropBox, page2.cropBox)

    if len(reader1.pages) > len(reader2.pages):
        if i >= len(reader2.pages):
            new_page.mergeTranslatedPage(page1, 0, (total_height - page1.mediaBox.upperRight[1]) / 2, False)
        else:
            new_page.mergeTranslatedPage(page1, 0, (total_height - page1.mediaBox.upperRight[1]) / 2, False)
            new_page.mergeTranslatedPage(page2, page1.mediaBox.upperRight[0], (total_height - page2.mediaBox.upperRight[1]) / 2, False)
    else:
        if i >= len(reader1.pages):
            new_page.mergeTranslatedPage(page2, 0, (total_height - page2.mediaBox.upperRight[1]) / 2, False)
        else:
            new_page.mergeTranslatedPage(page1, 0, (total_height - page1.mediaBox.upperRight[1]) / 2, False)
            new_page.mergeTranslatedPage(page2, page1.mediaBox.upperRight[0], (total_height - page2.mediaBox.upperRight[1]) / 2, False)
    
writer.write(open("./h-merged.pdf", "wb"))