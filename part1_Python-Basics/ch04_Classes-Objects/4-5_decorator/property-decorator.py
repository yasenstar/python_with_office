class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,new_age):
        if not new_age:
            return
        if not isinstance(new_age, int):
            return
        if new_age < 0:
            return
        self.__age = new_age

p1 = Person("Ice", 18)
print(p1.age)
p1.age = 20
print(p1.age)
p1.age = 30
print(p1.age)