# Light Copy - copy()

# import copy
# fruit1 = ["pineapple", "banana"]
# print(id(fruit1))
# fruit2 = copy.copy(fruit1)
# print(id(fruit2))
# fruit1[0] = "peach"
# print(id(fruit1))
# print(fruit2)
# print(id(fruit2))

# import copy
# fruit1 = ["pineapple", ["mobile", "computer"]]
# fruit2 = copy.copy(fruit1)
# print(id(fruit1), fruit1)
# print(id(fruit2), fruit2)
# fruit1[0]="apple"
# print(id(fruit1), fruit1)
# print(id(fruit2), fruit2)
# fruit1[1][0]="tablet"
# print(id(fruit1), fruit1)
# print(id(fruit2), fruit2)

# Deep Copy - deepcopy()

import copy
fruit1 = ["pineapple", ["mobile", "computer"]]
fruit2 = copy.deepcopy(fruit1)
print(id(fruit1), fruit1)
print(id(fruit2), fruit2)
fruit1[0]="apple"
print(id(fruit1), fruit1)
print(id(fruit2), fruit2)
fruit1[1][0]="tablet"
print(id(fruit1), fruit1)
print(id(fruit2), fruit2)