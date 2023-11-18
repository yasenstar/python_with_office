class MyError(Exception):
    def __init__(self,arg1,arg2):
        self.arg1 = arg1
        self.arg2 = arg2
    def __str__(self):
        return "self defined exception, arg1={}, arg2={}".format(self.arg1,self.arg2)
try:
    data1,data2=99,0
    if data2==0:
        raise MyError(data1,data2)
except MyError as e:
    print("MyError: {}".format(e))    
finally:
    print("no error")