def merge(start, mid, end):
    rN = end - mid
    lN = mid - start + 1
    lArr = [0] * lN
    rArr = [0] * rN
    for i in range(0, lN):
        lArr[i] = arr[start + i]

    for i in range(0, rN):
        rArr[i] = arr[i + mid + 1]
    a = start
    r = 0
    l = 0
    while r < rN and l < lN:
        if (rArr[r] < lArr[l]):
            arr[a] = rArr[r]
            r += 1
        else:
            arr[a] = lArr[l]
            l += 1
        a += 1

    while r < rN:
        arr[a] = rArr[r]
        a += 1
        r += 1
    while l < lN:
        arr[a] = lArr[l]
        a += 1
        l += 1


def mergeSort(start, end):
    if (start < end):
        mid = (start + end) // 2
        mergeSort(start, mid)
        mergeSort(mid + 1, end)
        merge(start, mid, end)


arr = [4, 5, 6, 1, 2, 3]
mergeSort(0, 5)
print(arr)