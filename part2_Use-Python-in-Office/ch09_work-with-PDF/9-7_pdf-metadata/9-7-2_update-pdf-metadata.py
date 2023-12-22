from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("./test1.pdf")

meta = reader.metadata

meta.update(
    {
        "/Author": "YASEN",
        "/Title": "My testing PDF file"
    }
)

writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.add_metadata(meta)

with open("./9-7-2.pdf", "wb") as f:
    writer.write(f)