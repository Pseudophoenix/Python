class Student:
    def __init__(self): # this is a constructor
        self.name='Alok'  # instance variables
        self.age=20
        self.marks=40
    def talk(self): # instance method
        print("HI I am ",self.name)
        print("My age is ",self.age)
        print("My marks are ",self.marks)

Alok=Student() # instantiating the object or creating the object
Alok.talk() # calling the talk method of Student class using . operator
