from PyPDF2 import PdfReader

# reader = PdfReader("./TSLA-Q3-2023-Update-3.pdf")
reader = PdfReader("./test1.pdf")

meta = reader.metadata

# print(type(meta), len(meta), meta.keys())

print(meta.author)

print(meta.creator)

print(meta.producer)

print(meta.title)

print(meta.subject)
