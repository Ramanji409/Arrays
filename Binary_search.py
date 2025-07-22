def binary_search(arr,target):
    arr.sort()
    low = 0 
    high =len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low=mid+1
        else:
            high=mid-1
    return "Taret Not Found"
arr=[4,2,6,3,1,9,8]
print(binary_search(arr,3))
