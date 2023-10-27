num = 666
print("outside func1: ", num, id(num))

def my_func1():
    print("my_func1: ", num, id(num))
    
def my_func2():
    global num
    num = 888
    print("my_func2: ", num, id(num))

my_func1()
my_func2()

print("outside func2: ", num, id(num))