class Person:
    def __init__(self):
        self.name="A"

    def display(self):
        print("Name=",self.name)

    class Dob:
        def __init__(self):
            self.dd=10
            self.mm=3
            self.yy=2001
        def display(self):
            print("DOB: {}/{}/{}".format(self.dd,self.mm,self.yy))

p=Person()
p.display()
x=Person.Dob()
x.display()
