class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        #prefix
        for i,num in enumerate(nums):
            if i == 0:
                continue
            
            res[i] = res[i-1]*nums[i-1]
        
        post_fix = 1

        for j in range(len(nums)-1,-1,-1):
            res[j] *= post_fix
            post_fix *= nums[j]
            
        return res