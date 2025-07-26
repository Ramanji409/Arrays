def subarray(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            print(arr[i:j+1])
arr=[1,2,3,4]
print(subarray(arr))