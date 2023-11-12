# 2.3.1 Create new list

# my_list1 = list()
# print(type(my_list1), my_list1)

# my_list2 = []
# print(type(my_list2), my_list2)

# my_list3 = ["A", "Hello", 2, 3, 4.5, ["a", "b", "c"]]
# print(type(my_list3), my_list3)
# print("my_list3 has {} elements".format(len(my_list3)))

# 2.3.2 Query

# type_list = [
#     "Fruit",
#     ["Apple", "Pear", "Banana", ["Yellow Banana", "Green Banana"], "Peach"],
#     "Device",
#     ["Mobile", "Computer", "Laptop", "Tablet"]
# ]

# print(type_list[0])
# print(type_list[1])
# print(type_list[1][2])
# print(type_list[1][3][0])
# print(type_list[-1])
# print(type_list[-1][2])
# print(type_list[1][-2])
# sub_list = type_list[0:2]
# print(sub_list)

# data_index = type_list[3].index("Computer")
# print(f"the 'computer', index is {data_index}")

# 2.3.3 Add Element - append(), insert()

# my_list = [1,2,3]
# print(my_list)
# my_list.append(4)
# print(my_list)
# my_list.append(5)
# print(my_list)
# my_list.append("hello")
# print(my_list)

# my_list = ['a', 'b', 'c']
# print(my_list)
# my_list.insert(10, 20.05)
# print(my_list)

# 2.3.4 modify element

# my_list = ['a', 'b', 'c']
# print(my_list)
# my_list[1]="B"
# print(my_list)

# 2.3.5 Delete Element from List: remove(), pop(), del

# my_list = ['a', 'b', 'b', 'b', 'b', 'c', 'd']
# print(my_list)
# my_list.remove("b")
# print(my_list)
# my_list.remove("b")
# print(my_list)
# my_list.pop(0)
# print(my_list)
# my_list.pop()
# print(my_list)
# my_list.pop(3)
# print(my_list)
# del my_list[2]
# print(my_list)
# del my_list
# print(my_list) # get error

# 2.3.6 Merge multiple list

# my_list2 = [1,2,3,4,5]
# # my_list3 = my_list + my_list2
# # print(my_list3)
# my_list4 = my_list2 * 4
# print(my_list4)

# Statistics in List Element

my_list = [1,2,3,3,3,3,3,3,3,3,4,5]
print(len(my_list))
print(min(my_list))
print(max(my_list))
print(my_list.count(3))
