def sort_func(sort_dict):
    age = sort_dict["age"]
    return age
info_list = [{"name":"pan","age":18},{"name":"icy","age":22},{"name":"zhao","age":
20}]
info_list.sort(key=sort_func)
print(info_list)
# 输出：[{'name':'pan','age':18},{'name':'zhao','age': 20},{'name':'icy','age':22}]
info_list.sort(key=sort_func,reverse=True)
print(info_list)
# 输出：[{'name':'icy','age':22},{'name':'zhao','age':  20},{'name':'pan','age':18}]