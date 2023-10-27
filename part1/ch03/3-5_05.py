def calculate(a, b, symbol="+"):
    rusult = None
    if symbol == "+":
        result = a + b
    else:
        print("wrong symbol")
    return result

my_params = [1,2,"+"]
print(calculate(*my_params))

my_params = {"a":1, "b": 3, "symbol":"+"}
print(calculate(**my_params))