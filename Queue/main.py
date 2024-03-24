class Queue:
    def __init__(self):
        self.Q=[]
    def display(self):
        if len(self.Q)==0:
            print("Empty Queue")
        else:
            print("Queue elements are",self.Q)
    def insert(self,element):
        self.Q.append(element)
    def delete(self):
        if len(self.Q) == 0:
            print("Empty Queue")
        else:
            element=self.Q[0]
            self.Q.remove(self.Q[0])
            return element
    def search(self,element):
        if len(self.Q)==0:
            print("EMPTY QUEUE")
        else:
            return self.Q.index(element)
    def sort(self):
        self.Q.sort()
        print(self.Q)

q=Queue()
choice=0
while choice<=5:
    print("QUEUE OPERATIONS")
    print("1 Display")
    print("2 Insert at rear")
    print("3 Delete from front")
    print("4 Search")
    print("5 Exit")
    choice=int(input("Enter the Choice: "))
    if choice==1:
        q.display()
    elif choice==2:
        element=int(input("Enter the element : "))
        q.insert(element)
    elif choice==3:
        element=q.delete()
        print("Removed ",element,"from front")
    elif choice==4:
        element=int(input("Enter element to search: "))
        pos=q.search(element)
        if pos==-1:
            print("Not Found")
        else:
            print("Element found at",pos)
    elif choice==5:
        q.sort()
    else:
        break