def division(a,b):
    try:
        print(f"try to execute, with parameter a:{a}, b:{b}")
        res = a / b
        return res
    except Exception as e:
        print("exception message is: ", e)

print(division(2,1))
print(division(2,"hahaha"))
print(division(2,0))
