# a = 3
# b = 3
# print(id(a), id(b))

# import copy
# c = ["A"]
# d = c.copy()
# print(id(c), id(d))
# print(id(c) == id(d))

a = 2
b = 2
print(a is b)
c = ["A"]
d = c.copy()
print(c == d)
print(c is d)
print(c is not d)