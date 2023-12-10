from os.path import basename, dirname, join
from docx import Document, ImagePart
path = "./7-9-1-test.docx"
doc = Document(path)

for p in doc.paragraphs:
    for image in p._element.xpath('.//pic:pic'):
        for img_id in image.xpath('.//a:blip/@r:embed'):
            part = doc.part.related_parts[img_id]
            if not isinstance(part, ImagePart):
                continue
            save_path = join(dirname(path), basename(part.partname))
            with open(save_path, "wb") as f:
                f.write(part.blob)