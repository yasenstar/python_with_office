class Person:
    hometown = "Earth"
    def __init__(self,name):
        self.name = name
    @classmethod
    def set_hometown(cls,new_hometown):
        cls.hometown = new_hometown

p1 = Person("personA")
p2 = Person("personB")

print(f"{p1.name}'s hometown is {p1.hometown}")
print(f"{p2.name}'s hometown is {p2.hometown}")

p1.set_hometown("M78 Planet")
p1.name = "new person1"

print(f"{p1.name}'s hometown is {p1.hometown}")
print(f"{p2.name}'s hometown is {p2.hometown}")
