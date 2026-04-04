class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0

        seen = set(nums)

        for num in nums:
            cnt = 0 

            if num-1 not in seen:
                while num + cnt in seen:
                    cnt += 1
                longest = max(longest, cnt)
        
        return longest 

