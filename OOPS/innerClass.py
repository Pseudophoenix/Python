class Person:
    class DOB:
        def __init__(self):
            self.dd = 3;
            self.mm = 3;
            self.yy = 2003;

        def display(self):
            print("DOB {}/{}/{}".format(self.dd, self.mm, self.yy))
    def __init__(self):
        self.name="A"
        self.db=self.DOB()

        def display():
            pass

p=Person()
# p.display()
x=p.db
x.display()