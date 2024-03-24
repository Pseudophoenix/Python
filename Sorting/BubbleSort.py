
arr=[2,7,3,9,1,4,6,8,5]

def Bubble():
    for i in range(0,8):
        for j in range(i+1,9):
            if(arr[i]<arr[j]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
Bubble()
print(arr)
arr.sort()
print(arr)
Bubble()
print(arr)
        