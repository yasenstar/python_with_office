f = None
try:
    f = open("./test.txt", "r", encoding="utf-8")
    # data = f.read()
    # data = f.readline()
    data = f.readlines()
    print(data)
    print(data[1])
except Exception as e:
    print("file reading failed: ", e)
finally:
    if f:
        f.close()