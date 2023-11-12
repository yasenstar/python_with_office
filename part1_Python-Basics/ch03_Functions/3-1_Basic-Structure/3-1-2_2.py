score = input("please tell me your exam result(0~100): ")
score = int(score)
print(f"your score inputs is {score}")

if 0 <= score <= 100:
    print(f"your score is {score}, good job")
else:
    print("input error")