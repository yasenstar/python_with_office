import fitz
import os
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
file_dir_select = filedialog.askdirectory() 
def pdf_merge_crop(file_dir_select):
    pdf =  [file for file in os.listdir(file_dir_select) if file.endswith('.pdf')]
    with fitz.open() as merge:
        for file in pdf:
            with fitz.open(file) as ft:
                merge.insert_pdf(ft)

        for page_index in range(len(merge)):
        
            page = merge[page_index]
            page.set_rotation(90)
            page.set_cropbox(fitz.Rect(58, 80, 570, 760))
            pix = page.get_pixmap(dpi=300) 
            pix.save("page%i.png" % page.number)

        merge.save('crop.pdf')