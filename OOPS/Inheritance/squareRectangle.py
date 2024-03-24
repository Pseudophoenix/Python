class Square:
    def __init__(self,x):
        self.x=x

    def area(self):
        print('Area of square=',self.x*self.x)

class Rectangle(Square):
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y

    def area(self):
        # super().area()
        print("Area of Rectangle is ",self.x*self.y)

a,b=[float(x) for x in input("Enter two numbers: ").split()]
r=Rectangle(a,b)
r.area()
