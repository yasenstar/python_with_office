class Person:
    def say(self):
        print("person speaks")
        
class Student(Person):
    def say(self):
        print("student speaks")

class Teacher(Person):
    def say(self):
        print("teacher speaks")

person = Person()
person.say()

student = Student()
student.say()

teacher = Teacher()
teacher.say()