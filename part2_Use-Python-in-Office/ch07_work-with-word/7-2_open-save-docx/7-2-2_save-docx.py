import os
from docx import Document

work_path = os.getcwd()
# print(work_path)

dir_name = "word_files_3"

file_name = "test1.docx"

target_dir = os.path.join(work_path,dir_name)
# print(target_dir)

if not os.path.exists(target_dir):
    os.makedirs(target_dir)
    # print(target_dir)

full_path = os.path.join(work_path, dir_name, file_name)
print(full_path)

doc = Document()

doc.save(full_path)