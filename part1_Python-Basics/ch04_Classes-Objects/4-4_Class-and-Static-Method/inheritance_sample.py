class Person:
    def __init__(self):
        self.name = "未知姓名 unknown name"
    def say(self):
        print("it's speaking from Person")

class Student(Person):
    def say(self):
        print("it's student speaking")
    def test(self):
        print("it's student doing the exam")
        
student = Student()
print(student.name)

student.say()
student.test()

print(isinstance(student, Student))
print(isinstance(student, Person))