class Person:
    def __init__(self,name,age=1):
        self.name = name
        self.age = age

p1 = Person("pan", 18)
p2 = Person("pan", 28)

print("Info of P1: ",id(p1),p1.name, id(p1.name),p1.age,id(p1.age))

print("Info of P2: ",id(p2),p2.name,id(p2.name),p2.age,id(p2.age))