class MyClass:
    n=0
    def __init__(self):
        MyClass.n=MyClass.n+1
    @staticmethod
    def noOfObj():
        print("No of Object are ",MyClass.n)

obj1=MyClass()
print(MyClass.noOfObj())
obj2=MyClass()
print(obj2.noOfObj())
obj3=MyClass()
print(obj3.noOfObj())