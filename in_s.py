def selection_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

arr=[23,1,12,31,56,32,30]
print(selection_sort(arr))