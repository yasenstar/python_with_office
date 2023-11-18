# from my_module import my_name, say_hello

import my_module

my_name = "new name"

print("my name is: ", my_module.my_name)

my_module.say_hello()
my_module.say_hello(my_name)