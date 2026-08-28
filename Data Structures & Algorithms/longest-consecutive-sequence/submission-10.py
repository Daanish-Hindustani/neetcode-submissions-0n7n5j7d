class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
         set_of_nums = set(nums)

         cnt = 0
         for num in set_of_nums:
            diff = 0
            while (num - diff) in set_of_nums:
               diff += 1
            
            cnt = max(cnt, diff)
      
         return cnt

