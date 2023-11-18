class Person:
    def __init__(self):
        self.age = None
    def set_age(self,new_age):
        if not new_age or not isinstance(new_age, int):
            raise TypeError ("type is incorrect, need integer")
        self.age = new_age

p = Person()
p.set_age("aa")
print(p.age)