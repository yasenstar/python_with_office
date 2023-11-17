class Person:
    def say(self):
        print("person speaks")
        
class Student(Person):
    def say(self):
        print("student speaks")

class Teacher(Person):
    def say(self):
        print("teacher speaks")

def do_something(somebody=Person()):
    somebody.say()

do_something(Person())
do_something(Student())
do_something(Teacher())