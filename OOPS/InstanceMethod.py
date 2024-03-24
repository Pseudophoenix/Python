class Student:
    def __init__(self,n='',m=0):
        self.name=n;
        self.marks=m;
    def display(self):
        print("Hi",self.name)
        print("Your marks are ", self.marks)
    def calculate(self):
        if(self.marks>=600):
            print("You got first grade")
        elif self.marks>=500:
            print("You got second grade")
        elif self.marks >= 400:
            print("You got third grade")
        else:
            print("You failed")
n=int(input("How many students: "))
i=0
while i<n:
    name=input("Enter your name: ")
    marks=int(input("Enter your marks: "))
    s=Student(name,marks)
    s.display()
    s.calculate()
    i+=1
    print("------------")
