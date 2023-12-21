from PyPDF2 import PdfMerger

merger = PdfMerger()

pdf1 = open("./test1.pdf", "rb")
pdf2 = open("./test2.pdf", "rb")
pdf3 = open("./test3.pdf", "rb")

merger.append("./test1.pdf")
merger.merge(position=0, fileobj=pdf2, pages=(1,2))
merger.merge(position=4, fileobj=pdf3, pages=(0,2))

merger.write("./9-3-3_2.pdf")
merger.close()