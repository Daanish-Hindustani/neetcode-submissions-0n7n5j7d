class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1

        temp = []
        for num in nums:
            temp.append(prefix)
            prefix *= num
        
        postfix = 1

        for i in range(len(nums)-1, -1, -1):
            temp[i] *= postfix
            postfix *= nums[i]
        
        return temp