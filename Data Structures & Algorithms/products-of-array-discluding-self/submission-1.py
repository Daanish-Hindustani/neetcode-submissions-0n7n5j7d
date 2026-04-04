class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multi = 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = multi
            multi *= nums[i]
        
        multi = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= multi
            multi *= nums[i]
        
        return res
