score = input("please tell me your exam result(0~100): ")
score = int(score)
print(f"your score inputs is {score}")

if score > 100:
    print("your input is invalid, too big")
    score = 100
    print(f"currnet score is {score}")
if score < 0:
    print("it's too small, invalid")
    score = 0
    print(f"current score is {score}")