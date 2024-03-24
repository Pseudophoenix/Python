# super().__init__()
# super().__init__(arguements)
# super().method()

# def __init__(self,property1=0,property=0):
#     super().__init__(property)
#     self.property1=property1
class Father:
    def __init__(self,property=0):
        self.property=property
    def display_property(self):
        print("Father\'s property is ",self.property)
class Son(Father):
    def __init__(self,property1=0,property=0):
        super().__init__(property)
        self.property1=property1

    def display_property(self):
        print("Total property of child=",self.property+self.property1)
s=Son(9000,80000)
s.display_property()