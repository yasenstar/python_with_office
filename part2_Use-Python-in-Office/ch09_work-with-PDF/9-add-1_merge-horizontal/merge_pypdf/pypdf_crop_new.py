from pypdf import PdfReader, PdfWriter, PdfMerger
from pypdf.generic import RectangleObject   # use for updating the page properties
import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_dir_select = filedialog.askdirectory()

merger = PdfMerger()

pdf_files = [file for file in os.listdir(file_dir_select) if file.endswith('.pdf')]
for file in pdf_files:
    merger.append(open(file,'rb'))

output = open('./output/merged.pdf','wb')
merger.write(output)

merger.close()
output.close()
    
writer = PdfWriter()

reader = PdfReader(open('./output/merged.pdf', "rb"))
# print(type(reader))

for i in range(len(reader.pages)):
    page = reader.pages[i]
    print(page.mediabox)
    
    page.rotate(90)
    print(page.mediabox)
    
    page.transfer_rotation_to_content()
    print(page.mediabox)
    
    # page.mediabox.upper_left= (58, 570)
    # page.mediabox.upper_right= (760, 570)
    # page.mediabox.lower_left= (58, 80)
    # page.mediabox.lower_right= (760, 80)    
    # print(page.mediabox)    
    
    writer.add_page(page)    
    
with open("./output/result.pdf", "wb") as ft:
    writer.write(ft)
    