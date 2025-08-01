def rotate(arr,d):
    new_array=[]
    for i in range(d,len(arr)):
        new_array.append(arr[i])
    new_array.extend(arr[:d])
    print(new_array)

arr=[3,1,4,6,2]
d=1
rotate(arr,d)
