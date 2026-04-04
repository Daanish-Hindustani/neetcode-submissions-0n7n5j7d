class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        seen = set(nums)

        for num in nums:
            if num -1 in seen:
                continue
            
            cnt = 0

            while num + cnt in seen:
                cnt += 1
            
            longest = max(longest, cnt)

        return longest