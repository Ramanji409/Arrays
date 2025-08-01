def second_highest(arr):
    if not arr:
        return 0
    arr.sort()
    k=1
    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            arr[k]=arr[i]
            k+=1
    return arr[k-2]
arr=[2,4,1,6,5,3,1,2,4,7]
print(second_highest(arr))