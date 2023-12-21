from PyPDF2 import PdfReader, PdfWriter

writer = PdfWriter()
reader = PdfReader("./test1.pdf")

for page in reader.pages[:2]:
    # writer.addPage(page)
    writer.add_page(page)
    
# PyPDF2.errors.DeprecationError: addPage is deprecated and was removed in PyPDF2 3.0.0.
# Use add_page instead.

with open("./9-3-2.pdf", "wb") as f:
    writer.write(f)