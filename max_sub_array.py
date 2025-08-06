def maxSubArray(nums):
        max_sub=current_sub=nums[0]
        for num in nums[1:]:
            current_sub=max(num,current_sub+num)
            max_sub=max(max_sub,current_sub)
        return max_sub
nums=[-1,3,2,-2,1,0,-4]
print(maxSubArray(nums))