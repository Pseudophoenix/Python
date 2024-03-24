class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks
n=int(input("How many students? \n:"))
i=0
while i<n:
    i+=1
    s=Student()
    name=input("Enter your name: ")
    s.setName(name)
    marks = input("Enter your marks: ")
    s.setMarks(marks)
    print('Hi ',s.getName())
    print('You got ', s.getMarks())
    print("----------------")