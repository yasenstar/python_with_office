# Data Structure - String

# char

# print(ord("A"))
# print(ord("a"))
# print(chr(65))
# print(chr(38))

# string

# a = 'hello'
# b = "another hello"
# c = '''Python'''
# d = """Python-2"""
# print(a, b, c, d)

# print("dafadfdafdsfada \n dfdsafdsafsadfa\nadfasfafd")

# print("""dafadfdaf
#       sfada \n dfdsafds
#       afsadfa\nadfasfafd""")

# print("It's very cool")
# print('It\'s very cool')

# print("C:\\Users\\admin\\Documents\\WeChat Files\\Applet")
# 输出：C:\Users\admin\Documents\WeChat Files\Applet
# print(r"C:\Users\admin\Documents\WeChat Files\Applet")
# 输出：C:\Users\admin\Documents\WeChat Files\Applet

# String Index

# my_str = "Of fice is very lucky, since she meets Python"
# print(my_str[0])
# print(my_str[-6])
# print(len(my_str))
# print(my_str[10:20])
# print(my_str[10::2])
# print(my_str.index("P"))
# print(my_str.index("Pyth"))
# print(my_str.find("z"))
# print(my_str.index("z"))

# String Join

# my_str1 = "hello "
# my_str2 = "world "
# my_str3 = "Python "
# my_str = my_str1 + my_str3 + my_str2
# print(my_str)
# print(my_str1, my_str3, my_str2, sep="___")

# char = "***--"
# print(char)
# print(char * 10)

# my_str = "hello"
# my_str1 = "--".join(my_str)
# print(my_str1)

# my_str = "hello world"
# new_str = my_str.replace(" ", " Python ")
# print(new_str)

# my_str = "Hello World"
# print(my_str.upper())
# print(my_str.lower())

# my_str = "Hello World"
# print(my_str.split(" "))

# my_str = "{1} is very lucky, she meets {0}"
# name1 = "Office"
# name2 = "Python"
# print(my_str)  # 输出：{}很幸运，她遇上了{}
# print(my_str.format(name1,name2))  # 输出：Of fice很幸运，她遇上了Python
# # print(my_str.format(name1))  # 报错
# new_str = f"{name1} is very lucky, she meets {name2} and happy"
# print(new_str)

# my_str = "%d年后, %s遇到了%s"
# print(my_str % (500,"Of fice","Python"))
# # 输出：5年后，Of fice遇到了Python

print("%.2f是圆周率的近似值" % 3.1415926)  # 输出：3.14是圆周率的近似值
print("增长比例高达%d%%" % 33.3)  # 输出：增长比例高达33%