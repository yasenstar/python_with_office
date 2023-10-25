score = input("please tell me your exam result(0~100): ")
score = int(score)
print(f"your score inputs is {score}")

if score >= 90:
    print("excellent")
elif score >= 80:
    print("very good")
elif score >= 70:
    print("well")
elif score >= 60:
    print("need more hard work")
else:
    print("not well")