# non-changeable type

# my_age = 18
# print(id(my_age))
# my_age = 20
# print(id(my_age))

# your_age = my_age
# print(id(your_age))

# my_name = "pan"
# your_name = my_name
# print(id(my_name), id(your_name))
# her_name = my_name.replace("p", "PAAA")
# print(my_name)
# print(id(my_name), id(her_name))

# a = 3 + 4j
# print(type(a))
# b = a
# print(id(a), id(b))
# a = 3 + 5j
# print(id(a))

# changeable type

# fruit_list = ["pineapple", "banana", "melon"]
# print(id(fruit_list))
# fruit_list[1] = "peach"
# print(fruit_list)
# print(id(fruit_list))

fruit1 = ["pineapple", "banana"]
fruit2 = fruit1
print(id(fruit1), fruit1)
print(id(fruit2), fruit2)
fruit1[0] = "peach"
print(fruit1)
print(id(fruit1), fruit1)
print(id(fruit2), fruit2)
print("\n")
fruit1 = ["pineapple", "banana"]
fruit2 = ["pineapple", "banana"]
print(id(fruit1), fruit1)
print(id(fruit2), fruit2)
fruit1[0] = "peach"
print(fruit1)
print(id(fruit1), fruit1)
print(id(fruit2), fruit2)