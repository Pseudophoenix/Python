"""Instance Variable Class Variable"""

# class Sample:
#     def __init__(self):
#         self.x=10
#     def modify(self):
#         self.x+=1
# s1=Sample()
# s2=Sample()
# print('x in s1=',s1.x)
# print('x in s2=',s2.x)
# s1.modify()
# print("After modification")
# print('x in s1=',s1.x)
# print('x in s2=',s2.x)

class Sample:
    x=10
    @classmethod # this is a decorator
    def modify(cls): # cls must be the first parameter
        cls.x+=1 # cls.x refers to the class variable x
s1=Sample()
s2=Sample()

print('x in s1=',s1.x)
print('x in s2=',s2.x)
s1.modify()
print("After Modification")
print('x in s1=',s1.x)
print('x in s2=',s2.x)
