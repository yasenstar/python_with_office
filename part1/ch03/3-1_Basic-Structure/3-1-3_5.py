import random
random_num = random.randint(0,100)
total_count = 10

left_count = total_count

is_correct = False

print("Game is started, you have total {} chances".format(total_count))

while left_count > 0:
    user_num = input(f"still have {left_count} chances, please guess: ")
    if not user_num.isdigit():
        print("please input one integer")
        continue
    user_num = int(user_num)
    if user_num > random_num:
        print("too big")
    elif user_num < random_num:
        print("too small")
    else:
        is_correct = True
        print("congratulation, the number is {}".format(random_num))
        break
    left_count = left_count - 1

if not is_correct:
    print(f"sorry, {total_count} changes have been used out! the correct number is {random_num}")