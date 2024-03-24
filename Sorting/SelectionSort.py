arr=[2,7,3,9,1,4,6,8,5]

def Selection():
    for i in range(0,8):
        # small=arr[i]
        for j in range(i+1,9):
            if(arr[i]>arr[j]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
Selection()
print(arr)
arr.sort()
print(arr)
Selection()
print(arr)
        