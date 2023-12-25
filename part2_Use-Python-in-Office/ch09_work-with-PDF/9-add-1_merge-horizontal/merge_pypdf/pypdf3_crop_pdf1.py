from pypdf import PdfMerger,PdfReader ,PdfWriter
from pypdf.generic import RectangleObject
import os
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
file_dir_select = filedialog.askdirectory() 
def pdf_merger(file_dir_select):
    pdf_files = [file for file in os.listdir(file_dir_select) if file.endswith('.pdf')]
    merger = PdfMerger()
    for file in pdf_files:
        merger.append(open(file,'rb'))
    
    with open('./合并2.pdf','wb') as ft:
        merger.write(ft)
    merger.close()

    writer1= PdfWriter()
    read1 = PdfReader(open('合并2.pdf','rb'))

    for i in range(len(read1.pages)):
        
        page = read1.pages[i]
        print(page.mediabox.lower_left, page.mediabox.lower_right, page.mediabox.upper_left, page.mediabox.upper_right)
        
        
        # Manually update page mediabox
        print(page.mediabox.lower_left, page.mediabox.lower_right, page.mediabox.upper_left, page.mediabox.upper_right)
        new_width = page.mediabox.upper_right[1]
        new_height = page.mediabox.upper_right[0]
        page.update({'/ArtBox': RectangleObject([0, 0, new_width, new_height])})
        page.update({'/BleedBox': RectangleObject([0, 0, new_width, new_height])})
        page.update({'/CropBox': RectangleObject([0, 0, new_width, new_height])})
        page.update({'/MediaBox': RectangleObject([0, 0, new_width, new_height])})
        page.update({'/TrimBox': RectangleObject([0, 0, new_width, new_height])})
        page.rotate(90)
        print(page.mediabox.lower_left, page.mediabox.lower_right, page.mediabox.upper_left, page.mediabox.upper_right)

        writer1.add_page(page)
        
    with open('旋转2.pdf','wb') as f :

        writer1.write(f)

    writer2 = PdfWriter()
    read2 = PdfReader(open('旋转2.pdf','rb'))

    for i in range(len(read2.pages)):

        page = read2.pages[i]

        # page.mediabox.upper_left= (0, 0)
        # page.mediabox.upper_right= (100, 0)
        # page.mediabox.lower_left= (0, 200)
        # page.mediabox.lower_right= (200, 300)
        
        page.mediabox.upper_left= (58, 570)
        page.mediabox.upper_right= (760, 570)
        page.mediabox.lower_left= (58, 80)
        page.mediabox.lower_right= (760, 80)
        
        page.apply_redactions()

        writer2.add_page(page)

        with open('裁剪2.pdf','wb') as ft :

            writer2.write(ft)
            
pdf_merger(file_dir_select) 
        
        

