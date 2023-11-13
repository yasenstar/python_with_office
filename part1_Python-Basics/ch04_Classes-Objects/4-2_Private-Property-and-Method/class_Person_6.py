class Person:
    def __init__(self, name, age=1):
        self.name = name
        self.__age = age
    def get_age(self):
        return self.__age
    def set_age(self, new_age):
        if not new_age:
            print("not existed")
            return
        if not isinstance(new_age, int):
            print("age must be integer")
            return
        if new_age < 0:
            print("age must over 0")
            return
        self.__age = new_age
        
p = Person("ice", 20)
print(p.name)
# print(p.age) will have error: 'Person' object has no attribute 'age'
print(p.get_age())
p.set_age("aaa")
print(p.get_age())
p.set_age(-5)
print(p.get_age())
p.set_age("")
print(p.get_age())
p.set_age(30)
print(p.get_age())
# print(p.__age)    error: 'Person' object has no attribute 'age'
print("Access private property: ", p._Person__age)