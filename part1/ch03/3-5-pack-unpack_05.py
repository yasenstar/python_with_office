def fun1(a,b,c):
    print(a,b,c)
    
def fun2(*args):
    args = list(args)
    # Modify args value
    args[0] = "Geeksforgeeks"
    args[1] = "awesome"
    
    fun1(*args)

fun1("Hello", "This", "World")

fun2("Hello", "This", "World")