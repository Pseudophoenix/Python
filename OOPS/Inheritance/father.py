class Father:
    def __init__(self):
        self.property=80000

    def display_property(self):
        print('Father\'s Property = ',self.property)

class Son(Father):
    pass
s=Son()
s.display_property()