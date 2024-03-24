import math
class Sample:
    @staticmethod
    def calculate(x):
        res=math.sqrt(x)
        return res
num=float(input("Enter a number: "))
res=Sample.calculate(num)
print("Sqrt of {} is {:.2f}".format(num,res))