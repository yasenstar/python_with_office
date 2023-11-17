class Person:
    def __init__(self,name):
        self.name = name
    def multiply(cls,a,b):
        return a * b
    @staticmethod
    def plus(a,b):
        return a + b

p1 = Person("Ice")
print(p1.multiply(3,4))
print(p1.plus(4,5))

print(Person.multiply(Person, 3,4))
print(Person.plus(4,5))