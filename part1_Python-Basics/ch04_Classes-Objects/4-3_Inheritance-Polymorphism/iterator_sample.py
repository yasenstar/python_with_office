from collections.abc import Iterable,Iterator

class MyList:
    def __init__(self):
        self.__list = list()
        self.__index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.__index < len(self.__list):
            data = self.__list[self.__index]
            self.__index += 1
            return data
        else:
            raise StopIteration
    def add_data(self,data):
        if isinstance(data,str) and data not in self.__list:
            self.__list.append(data)
    def __str__(self):
        return str(self.__list)
    
my_list = MyList()
print(my_list)
my_list.add_data("Python")
print(my_list)
my_list.add_data(1)
print(my_list)
my_list.add_data("of fice")
print(my_list)
my_list.add_data("Python")
print(my_list)
my_list.add_data("Hello")
print(my_list)
print(isinstance(my_list,Iterable))
print(isinstance(my_list,Iterator))

for i in my_list:
    print("current traverse value is ", i)