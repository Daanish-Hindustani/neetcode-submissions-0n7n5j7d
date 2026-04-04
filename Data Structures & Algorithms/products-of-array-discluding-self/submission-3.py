class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = [1] * len(nums)

        #prefix
        for i, num in enumerate(nums):
            if i == 0:
                continue
            
            temp[i] = nums[i-1] * temp[i-1]
        post_fix = 1
        for j in range(len(nums)-1,-1,-1):
            if j == len(nums)-1:
                post_fix *= nums[j]
                continue
            
            temp[j] *= post_fix
            post_fix *= nums[j]
        
        return temp
                
        return temp