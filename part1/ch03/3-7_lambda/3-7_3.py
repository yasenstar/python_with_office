# lambda [arg1 [,arg2, ...]]: expression

num_list = [12,5,1,8,55,6,]
num_list.sort()  # 默认正序
print(num_list)  # 输出：[1,5,6,8,12,55]
num_list.sort(reverse=True)  # 逆序
print(num_list)  # 输出：[55,12,8,6,5,1]