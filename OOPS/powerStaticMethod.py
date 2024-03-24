class MyClass:
    @staticmethod
    def mymethod(x,n):
        res=x**n
        print("{} to power {} is {}".format(x,n,res))
MyClass.mymethod(2,4)
MyClass.mymethod(3,2)