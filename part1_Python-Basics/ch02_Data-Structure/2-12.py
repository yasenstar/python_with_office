# Comprehensions

# List Comprehensions

# # tradition way using for loop
# my_list = [66,77,88]
# new_list = list()
# for data in my_list:
#     new_list.append(data * 2)
# print(my_list)
# print(new_list)

# # using comprehensions

# syntax: new_list = [expression for_loop_expression if condition]

# my_list = [66,77,88]
# print(my_list)
# new_list = [data * 2 for data in my_list]
# print(new_list)

# old_list = [0,1,2,3,4,5,6,7,8]
# print(old_list)
# new_list = []
# for item in old_list:
#     if item % 2 == 0:
#         new_list.append(item)
# print(new_list)

# old_list = [0,1,2,3,4,5,6,7,8]
# print(old_list)
# new_list = [item for item in old_list if item % 2 == 0]
# print(new_list)

# Dict Comprehensions

# my_list = [66,77,88]
# my_dict = {
#     key * 3:f"value {key * 3}" for key in my_list
# }
# print(my_dict)

# syntax: new_dict = { key_expr: value_expre for_loop_expression if condition}

# sample to find which students got full score in math

# old_student_score_info ={
#     "jack": {
#         "chinese": 87,
#         "math": 99,
#         "english": 95
#     },
#     "tom": {
#         "chinese": 100,
#         "math": 100,
#         "english": 92    
#     }
# }
# print(old_student_score_info)
# new_student_score_info = {
#     name: scores for name, scores in old_student_score_info.items() if scores["math"]==100
# }
# print(new_student_score_info)

# Set Comprehensions

# syntax: new_set = { expression for_loop_expr if condition}

# old_list = [0,1,3,3,4,3,6,3,8]
# print(old_list)
# new_set = {item for item in old_list if item % 2 == 0}
# print(new_set)

# Generator Comprehensions

my_list = [66,77,88]
my_generator = (item*2 for item in my_list)
print(my_list)
print(my_generator)
for x in my_generator: print(x)