from PyPDF2 import PdfReader

reader = PdfReader("./test1.pdf")

# print(reader.getNumPages())
# Error and Explanation:
# PyPDF2.errors.DeprecationError: 
# reader.getNumPages is deprecated and was removed in PyPDF2 3.0.0. 
# Use len(reader.pages) instead.

print(len(reader.pages))

# page = reader.getPage(0)
# print(type(page))
# Error and Explanation:
# PyPDF2.errors.DeprecationError: reader.getPage(pageNumber) is deprecated and was removed in PyPDF2 3.0.0.
# Use reader.pages[page_number] instead. 

print(type(reader.pages[0]))