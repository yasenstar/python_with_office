class Person:
    pass  

def calculate(a,b):
    print("is calling calculate method")
    return a + b

p1 = Person()

p1.name = "ice"

print("p1.name is: {}".format(p1.name))

p1.say = calculate

cal_result = p1.say(1,2)

print("calculation result is: {}".format(cal_result))