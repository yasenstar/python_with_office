class Person:
    def __init__(self,name,age=1):
        self.name = name
        self.age = age
    def say(self):
        increment = self.calculate(self.age,-18)
        print("hello, my name is {}, I'm {} years old, and I've been adult for {} years".format(self.name, self.age, increment))
    def calculate(self,a,b):
        return a + b    

p1 = Person("Yasen", 23)
p1.say()

cal_result = p1.calculate(23,-18)
print("calculation result is: {}".format(cal_result))