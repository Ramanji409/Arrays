#Linear Search
def linear_search(arr,target):
  n=len(arr)
  for i in range(n):
    if arr[i] == target:
      print(i)
      
arr=[3,6,1,7,9,2,8]
target=7
linear_search(arr,target)

#Binary Search
def binary_search(arr,target):
    arr.sort()
    low=0
    high=len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
           return mid
        elif arr[mid] < target:
           low=mid+1
        else:
           high=mid-1
    return -1
arr=[3,6,1,7,9,2,8]
target=9
print(binary_search(arr,target))

#Bubble_sort
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[6,3,8,1,9,10,5,4]
print(bubble_sort(arr))

#selection sort
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i 
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
arr=[45,12,27,31,50,10]
print(selection_sort(arr))

#insert sort
def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr
arr=[3,1,4,6,2,5]
print(insertion_sort(arr))

#Missing_number
def missing_number(arr,n):
    Expected_total=n*(n+1)//2
    actual_total=sum(arr)
    return Expected_total - actual_total
    
arr=[2,4,1,7,6,3]
print(missing_number(arr,7))

#Two Pointers
def two_pointers(arr,target):
    pairs=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                continue
            elif arr[i]+arr[j] == target:
                pairs.append((i,j))
    return pairs
arr=[2,4,6,9,5,1]
target=10
print(two_pointers(arr,target))

#Diognal_difference
def diognal_difference(matrix):
    n=len(matrix)
    first_diognal=sum(matrix[i][i] for i in range(n))
    second_diognal=sum(matrix[i][n-i-1] for i in range(n))
    ads_difference=first_diognal-second_diognal
    return ads_difference
matrix=[[13,16,14],[15,110,17],[18,1,234]]
print(diognal_difference(matrix))