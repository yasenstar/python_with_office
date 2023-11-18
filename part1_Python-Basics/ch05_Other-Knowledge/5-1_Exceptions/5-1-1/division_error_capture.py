def division(a,b):
    try:
        print(f"try to execute, with parameter a:{a}, b:{b}")
        res = a / b
        return res
    except TypeError as e:
        print("error found, please give correct data type")
        print("exception message is: ", e)
    except ZeroDivisionError as e:
        print("error found, you cannot divided by 0")
        print("exception message is: ", e)
    finally:
        print("function is finished")

print(division(2,1))
print(division(2,"hahaha"))
print(division(2,0))
