import json
f = None
try:
    f = open("./test1.txt", "w", encoding="utf-8")
    my_dict = {"A":1, "B":2, "C":3}
    f.write(json.dumps(my_dict))
except Exception as e:
    print("file processing failed: ", e)
finally:
    if f:
        f.close()
               