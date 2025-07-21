def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            print(i)

arr=list(map(int,input("Enter array:").split(",")))
target=int(input("Enter Number"))
linear_search(arr,target)