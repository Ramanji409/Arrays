def missing_number(arr,n):
    total_sum = n * (n+1) //2
    actual_sum = sum(arr)
    print(total_sum - actual_sum)

arr=[1,2,4,5,6,7,8,9,10]
missing_number(arr,10)