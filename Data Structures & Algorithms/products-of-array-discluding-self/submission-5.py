class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Goal: We want an array2 such that each ith index of array2 is the product of all indexed values except i in array1

        1. Prefix vs postfix
        """

        res = [1]*len(nums)

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1

        for j in range(len(nums)-1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
        
        return res