def odd_even_count(arr):
    even=0
    odd=0
    for nums in arr:
        if nums % 2 == 0:
            even +=1
        else:
            odd+=1
    return odd,even
arr=[2,4,1,6,3,5,7,9]
print(odd_even_count(arr))