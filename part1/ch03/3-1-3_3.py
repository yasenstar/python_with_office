import random
for i in range(10):
    rand_int = random.randint(0,100)
    print(f"current in #{i} loop")
    print(rand_int)
    if rand_int % 5 == 0:
        break
# print(rand_int)