class Stack:
    def __init__(self):
        self.st=['Alok','You']
    def isempty(self):
        return self.st==[]
    def push(self,element):
        self.st.append(element)
    def pop(self):
        if self.isempty():
            return  -1
        else:
            return self.st.pop()
    def peep(self):
        n=len(self.st)
        return self.st[n-1]
    def search(self,element):
        if self.isempty():
            return -1
        else:
            try:
                n=self.st.index(element)
                return  len(self.st)-n
            except ValueError:
                return -2
    def display(self):
        return self.st

S=Stack()
choice=0
while choice<5:
    print("Stack Operation")
    print("1 Push Element")
    print("2 Pop Element")
    print("3 Peep Element")
    print("4 Search for Elements")
    print("5 Exit")
    choice=int(input("YOUR CHOICE: "))
    if choice==1:
        element=int(input("Enter element:"))
        S.push(element)
    elif choice==2:
        element=S.pop()
        if element==-1:
            print("Stack is empty")
        else:
            print("Removed",element)
    elif choice==3:
            element=S.peep()
            print("Topmost Element",element)
    elif choice==4:
            element=input("Enter element")
            pos=S.search(element)
            if pos==-1:
                print("Empty Stack")
            elif pos==-2:
                print("Stack is Emptu")
            else:
                print("Element found at position :",pos)
    else:
        break
    print("Stack=",S.display())
