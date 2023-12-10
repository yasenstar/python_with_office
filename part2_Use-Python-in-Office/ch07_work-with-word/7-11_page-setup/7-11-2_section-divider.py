from docx import Document
from docx.enum.section import WD_SECTION_START

doc = Document()

s1 = doc.add_section()
print(s1.start_type)

s2 = doc.add_section(WD_SECTION_START.NEW_PAGE)
print(s2.start_type)

s3 = doc.add_section(WD_SECTION_START.CONTINUOUS)
print(s3.start_type)

s4 = doc.add_section(WD_SECTION_START.EVEN_PAGE)
print(s4.start_type)

s5 = doc.add_section(WD_SECTION_START.ODD_PAGE)
print(s5.start_type)