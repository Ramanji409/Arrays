            
def find_pairs(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                    continue
            
            elif nums[i]+nums[j] == target:
                print(i,j)
nums=[0,4,2,5,6]
find_pairs(nums,7)
