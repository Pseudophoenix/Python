arr=[2,7,3,9,1,4,6,8,5]

def Insertion():
    for i in range(1,9):
        # small=arr[i]
        temp=arr[i]
        j=i-1
        while j>=0 and temp<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp

Insertion()
print(arr)
arr.sort()
print(arr)
        