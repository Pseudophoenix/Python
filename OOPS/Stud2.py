"""Class and Object instantiation Constructor __init__ method"""
class Student:
    def __init__(self,n='',m=0):
        self.name=n;
        self.marks=m;
    def display(self):
        print('Hi ',self.name)
        print('Your marks are ',self.marks)

sunil=Student()
sunil.display()
akhil=Student("Akhil",80)
akhil.display()