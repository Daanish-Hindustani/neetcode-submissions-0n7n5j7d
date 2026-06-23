class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
         
         hashed_values = set(nums)
         max_value = 0

         for num in hashed_values:
            i = 0
            while num - i in hashed_values:
               i += 1
            
            max_value = max(i, max_value)

         return max_value
            
