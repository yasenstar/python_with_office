import os
from win32com import client

def doc_to_docx(path):
    print("Path: {}".format(path))
    if not os.path.isabs(path):
        print(f"not absolute path")
        return
    if not os.path.exists(path):
        print("sorry, file is not found")
        return
    if os.path.splitext(path)[1] != ".doc":
        print("file type is incorrect, not DOC which is expected")
        return
    app = client.Dispatch('Word.Application')
    app.DisplayAlerts = False
    document = app.Documents.Open(path)
    document.SaveAs(os.path.splitext(path)[0] + ".docx", 12)
    document.Close()
    app.Quit()

if __name__ == '__main__':
    work_path = os.getcwd()

    # dir_name = ""

    file_name = "test.doc"

    # target_dir = os.path.join(work_path,dir_name)
    # print(target_dir)

    # if not os.path.exists(target_dir):
    #     os.makedirs(target_dir)

    # full_path = os.path.join(work_path, dir_name, file_name)
    
    full_path = os.path.join(work_path, file_name)
    
    doc_to_docx(full_path)