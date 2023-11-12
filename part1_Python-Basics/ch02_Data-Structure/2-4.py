# 2.4.1 Create new Tuple

# my_tuple1 = tuple()
# print(type(my_tuple1), my_tuple1)

# my_tuple2 = (1,2,3)
# print(type(my_tuple2), my_tuple2)

# my_tuple3 = (1)
# print(type(my_tuple3), my_tuple3)

# my_tuple4 = (1,)
# print(type(my_tuple4), my_tuple4)

# 2.4.2 Access Tuple

my_tuple = ('python', 5, True, True, ["aa", 6], (3, 25))
# print(len(my_tuple))
# print(my_tuple[0])
# new_tuple = my_tuple[2:-1]
# print(new_tuple)
# my_tuple[3][0] = "AA"
# print(my_tuple)
print(my_tuple.count(True))
print(my_tuple.index(True))