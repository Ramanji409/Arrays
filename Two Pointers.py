def find_pairs(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                    continue
            
            elif nums[i]+nums[j] == target:
                print(i,j)
nums=[0,4,2,5,6]
find_pairs(nums,7)


#another way
def find_pairs(arr,target):
        seen={}
        for index,num in enumerate(arr):
            complement=target-num
            if complement in seen:
                return [seen[complement],index]
            seen[num]=index
        return []  
arr=[3,5,1,6,2,4]
target=7
print(find_pairs(arr,target))