from PyPDF2 import PdfMerger

merger = PdfMerger()

merger.append("./test1.pdf")
merger.append("./test3.pdf")
merger.append("./test2.pdf")
merger.write("./9-3-3_1.pdf")

merger.close()