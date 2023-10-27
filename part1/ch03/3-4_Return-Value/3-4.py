def calculate(a, b, symbol="+"):
    result = None
    if symbol == "+":
        result = a + b
    else:
        print("wrong symbol")
    return result

res1 = calculate(2, 43, "+")
print(res1)