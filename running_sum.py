def running_sum(nums):
    result=[]
    result.append(nums[0])
    for i in range(1,len(nums)):
        result.append(result[i-1]+nums[i])
    return result

nums=[1,2,3,4]
print(running_sum(nums))