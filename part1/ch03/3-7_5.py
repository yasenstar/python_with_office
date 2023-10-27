info_list = [{"name":"pan","age":18},{"name":"icy","age": 22},{"name":"zhao","age":
20}]
info_list.sort(key=lambda sort_dict:sort_dict["age"])
print(info_list)
# 输出：[{'name':'pan','age':18},{'name':'zhao','age': 20},{'name':'icy','age':22}]