def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[4,2,8,7,1,0]
print(bubble_sort(arr))
