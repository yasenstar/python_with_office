# 2.5.1 new create dict

# my_dict1 = dict()
# print(type(my_dict1), my_dict1)
# my_dict2 = {}
# print(type(my_dict2), my_dict2)

# my_dict = {
#     "A":1,
#     2:"2",
#     3.0:3,
#     True:"4",
#     (1,):5
# }
# print(type(my_dict), my_dict)

# 2.5.2 access elements in dict

# my_dict = {
#     "name": "pan",
#     "age": 18,
#     "height": " unknown"
# }

# # name = my_dict["name"]
# # print(name)
# # print(my_dict["age"])
# # print(my_dict["height"])
# # print(my_dict["gender"])

# # get() method
# # gender = my_dict.get("gender","confidential")
# # print(gender)
# print(my_dict)
# # # address = my_dict.get("address")
# # # print(type(address), address)
# # # address = my_dict.get("address","somewhere")
# # # print(type(address), address)

# # print(my_dict.keys())
# # print(my_dict.values())
# # print(my_dict.items())

# # 2.5.3 add elements into Dict

# # my_dict["gender"] = "male"
# # print(my_dict)
# # my_dict["phone"] = 1234567890
# # print(my_dict)

# my_dict.update(
#     {
#         "gender": "male",
#         "phone": 12345654564,
#         "address": "somewhere"
#     }
# )
# print(my_dict)

# you can also use setdefault()

# 2.5.4 modify dict's element

# my_dict = {"name":"pan","age":18,"height":"未知"}
# print(my_dict["age"])  # 输出：18
# my_dict["age"] = 25
# print(my_dict["age"])  # 输出：19

# also can use update() to modify

# 2.5.5 delete elements from dict

my_dict = {"name":"pan","age":18}
# del my_dict["age"]
# print(my_dict)  # 输出：{'name':'pan'}
# del my_dict["height"]  # 报错：KeyError:'height'

my_dict.update({"height":"unknown"})
print(my_dict)
# del_data1 = my_dict.pop("age")
# print(del_data1, my_dict)
# # del_data1 = my_dict.pop("gender")
# my_dict.pop("phone")

my_dict.clear()
print(my_dict)