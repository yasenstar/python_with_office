# my_list = [66,77,88,99]
# for x in my_list:
#     print(x)
#     print("end of this time's loop")
    
my_list = [66,77,88,99]
for i, x in enumerate(my_list): # if not using enumerate, get error "TypeError: cannot unpack non-iterable int object"
    print(f"current index is {i}")
    print(f"current element is {x}")
    print(f"current element times 2 is {x*2}")
print(my_list)