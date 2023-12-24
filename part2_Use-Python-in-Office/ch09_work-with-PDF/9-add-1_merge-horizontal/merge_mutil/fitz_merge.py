import fitz 

def merge_pdfs(output_file):
    merge = fitz.open()

    pdf1 = fitz.open('a.pdf') 
    pdf2 = fitz.open('b.pdf') 

    num = max(pdf1.page_count, pdf2.page_count) 
    # print(num)
    for i in range(num):
        page1 = pdf1[i] 
        page2 = pdf2[i] 

        width = int(page1.rect.width + page2.rect.width) 
        height = int(max(page1.rect.height, page2.rect.height)) 

        blank_page = merge.new_page(width, height)

        blank_page.show_pdf_page((0, 0, int(page1.rect.width), int(page1.rect.height)), pdf1, i,keep_proportion=True, rotate=90 )
        blank_page.show_pdf_page((int(page1.rect.width), 0, width, int(page2.rect.height)), pdf2, i, keep_proportion=True, rotate=90 )

    merge.save(output_file)
    merge.close()

merge_pdfs('merged_file.pdf')