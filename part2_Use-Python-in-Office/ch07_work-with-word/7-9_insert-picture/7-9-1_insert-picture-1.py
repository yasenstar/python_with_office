from docx import Document
doc = Document()

pic = doc.add_picture("./galaxy.jpg")

print(type(pic))

print(pic.type)

doc.save("./7-9-1-test.docx")