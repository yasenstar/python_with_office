def get_info():
    name = "Pan"
    age = 18
    # height = 170
    return name, age

name, age, height = get_info()
print(name, age, height)

# ValueError: not enough values to unpack (expected 3, got 2)