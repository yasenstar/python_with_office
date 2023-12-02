from passwordprotection import encrypt_excel

path = r"D:\GitHub\python_with_office\part2_Use-Python-in-Office\ch06_work-with-excel\6-11_protect-in-excel\test.xlsx"

encrypt_excel(path, "456", "", read_only_pwd="") 
