from collections.abc import Iterable, Iterator

class MyList:
    def __init__(self):
        self.__list = list()
    def __iter__(self):
        pass
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
print(isinstance(my_list,Iterable))
print(isinstance(my_list,Iterator))