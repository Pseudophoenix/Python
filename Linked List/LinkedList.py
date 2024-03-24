ll=[]
ll.append("America")
ll.append("Japan")
ll.append("India")
for i in ll:
    print(i)
print("The existing list = ",ll)
choice=0
while choice<5:
    print("Linked List Operations")
    print("1. Add Element")
    print("2. Remove Element")
    print("3. Replace Element")
    print("4. Search for Element")
    print("5. Exit")
    choice=int(input("Your choice: "))
    if(choice==1):
        element=input("Enter element: ")
        pos=int(input("At what position"))
        ll.inswer(pos,element)
    elif choice==2:
        try:
            element=input("Enter element: ")
            ll.remove(element)
        except ValueError:
            print("element not found")
    elif choice==3:
        element=input("Enter new element: ")
        pos=int(input("At what position:"))
        ll.pop(pos)
        ll.insert(pos,element)
    elif choice==4:
        element=int(input("Enter element: "))
        try:
            pos=ll.index(element)
            print("Element found at ",pos)
        except ValueError:
            print("Element not found")
    else:
        break
    print("List=",ll)