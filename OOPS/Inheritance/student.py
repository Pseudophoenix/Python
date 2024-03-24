from teacher import Teacher
class Student(Teacher):
    def setmarks(self,marks):
        self.marks=marks
    def getmarks(self):
        return self.marks

suman=Student()
suman.setid(456)
suman.setname("Suman")
# suman.setsalary(9000)
suman.setaddress("Old House","Boston")
suman.setmarks(89)

print("ID={} Name={} Marks={}".format(suman.getid(),suman.getname(),suman.getmarks()))
print(f"Address=")
suman.add.display()
