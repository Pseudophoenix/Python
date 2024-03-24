class Teacher:
    class ADD:
        def __init__(self,city,street):
            self.city=city
            self.street = street

        def display(self):
            print(self.city,self.street)

        def getcity(self):
            return self.city

        def getstreet(self):
            return self.street

    def setid(self,id):
        self.id=id

    def getid(self):
        return self.id

    def setname(self,name):
        self.name=name

    def getname(self):
        return self.name

    def setaddress(self,street,city):
        self.add=Teacher.ADD(street,city)

    def setsalary(self,salary=6000):
        self.salary=salary

    def getsalary(self):
        return self.salary

# t1=Teacher()
# t1.setid(45)
# t1.setname("Alok")
# t1.setaddress('Dharuhera',"Santosh Colony")
# t1.setsalary(9000)
# print("ID={}\nName={}\nSalary={}\nAddress={}, {}".format(t1.getid(),t1.getname(),t1.getsalary(),t1.add.getstreet(),t1.add.getcity()))
# t1.add.display()
