def remove_duplicate(arr):
    if not arr:
        return 0
    arr.sort()
    k=1
    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            arr[k]=arr[i]
            k+=1
    return k , arr[:k]
arr=[2,5,1,7,3,0,6,8,5,2,13,2]
print(remove_duplicate(arr))