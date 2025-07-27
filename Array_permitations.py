def array_permitations(arr):
    result=[]
    for i in range(len(arr)):
        result.append(arr[arr[i]])
    return result

arr=[0,2,4,1,3]
print(array_permitations(arr))