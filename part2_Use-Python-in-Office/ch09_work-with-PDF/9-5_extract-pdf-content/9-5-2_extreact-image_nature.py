import os
import fitz

pdf = fitz.open("./nature.pdf")

save_path = "./pdf_images_nature"

for index, page in enumerate(pdf.pages()):
    print(f"load the No. {index+1} page successfully!")
    for image in page.get_images():
        xref = image[0]
        print(xref)

        pix = fitz.Pixmap(pdf, xref)

        if not os.path.exists(save_path):
            os.mkdir(save_path)

        path = os.path.join(save_path, f"page{index+1}_{xref}.png")

        pix.save(path)