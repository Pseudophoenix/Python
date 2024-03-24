class Father:
    def __init__(self):
        self.property=89000
    def display(self):
        print("Father\'s property is ",self.property)

class Son(Father):
    def __init__(self): # constructor overriden
        self.property=800
    def display(self): # method overriden
        print("Son\'s property is ", self.property)

s=Son()
s.display()