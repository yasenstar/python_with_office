# 2.6.1 new create a set

# my_set1 = set()
# print(type(my_set1), my_set1)

# my_set2 = {12,12,True,"12"}
# print(type(my_set2), my_set2)

# fruit_list = ["peach", "watermelon", "banana", "watermelon"]
# print(type(fruit_list), fruit_list)
# temp_set = set(fruit_list)
# print(type(temp_set), temp_set)
# fruit_list = list(temp_set)
# print(type(fruit_list), fruit_list)

# 2.6.2 operating sets

## using symbol
# my_set1 = {1,2,3,4,5}
# my_set2 = {2,3,4}
# # # intersection
# # my_set3 = my_set1 & my_set2
# # print(type(my_set3), my_set3)
# # # differenct
# # print(my_set1 - my_set2)
# # # union
# # print(my_set1 | my_set2)
# # # supplement
# # print(my_set1 ^ my_set2)
# # # compare
# # print(my_set1 > my_set2)
# # print(my_set1 >= my_set2)
# # print(my_set1 == my_set2)
# # print(my_set1 <= my_set2)
# # print(my_set1 < my_set2)

# ## use natural language names
# # my_set3 = my_set2.intersection(my_set1)
# # print(my_set3)
# # print(my_set1.difference(my_set2))
# # print(my_set2.difference(my_set1))
# # print(my_set1.union(my_set2))
# print(my_set2.issubset(my_set1))
# print(my_set1.issubset(my_set2))

# add / delete element in set

# my_set = set()
# my_set.add('watermelon')
# print(my_set)
# my_set.add('watermelon')
# print(my_set)
# my_set.add('apple')
# print(my_set)
# my_set.update(["watermelon","Hamimelon"])
# print(my_set)

# del_data = my_set.pop()
# print(del_data)
# print(my_set)

my_set = {'peach', 'hamimelon', 'watermelon'}
print(my_set)
# my_set.discard('hamimelon')
# print(my_set)
# my_set.discard('apple')
# print(my_set)
# my_set.remove('hamimelon')
# print(my_set)
# my_set.remove('apple')
# print(my_set)
my_set.clear()
print(type(my_set),my_set)