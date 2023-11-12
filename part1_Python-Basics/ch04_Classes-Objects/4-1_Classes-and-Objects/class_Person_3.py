class Person:
    def __init__(self,name,age=1):
        self.name = name
        self.age = age

p1 = Person("pan", 18)
print("Original Age is: ", p1.age, type(p1.age))
p1.age = 20
print("Updated age now is: ", p1.age, type(p1.age))
p1.age = "unknown"
print("Updated age now is: ", p1.age, type(p1.age))
p1.height = 180
print("height is: ", p1.height)

p2 = Person("yasen", 20)
print(p2.height)