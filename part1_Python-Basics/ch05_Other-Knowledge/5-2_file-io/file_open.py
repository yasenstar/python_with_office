f = None
try:
    f = open("./test.txt", "w", encoding="utf-8")
    f.write("hello Yasen good day \n")
    f.writelines(["Python", "Office"])
except Exception as e:
    print("file operation failed: ", e)
finally:
    if f:
        f.close()