class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                lenght = 0
                while num + lenght in nums_set:
                    lenght +=1
                longest = max(lenght, longest)
        
        return longest