class MyClass:
    def __del__(self):
        print("execute till __del__")
    def say(self):
        print("auto calling 'say'")
    def __new__(cls, *args, **kwargs):
        print("execute till __new__")
        return super().__new__(cls, *args, **kwargs)
    def __init__(self):
        print("execute till __init__")
    def saynew(self):
        print("auto calling 'saynew'")

c = MyClass()
c.say()
c.saynew()