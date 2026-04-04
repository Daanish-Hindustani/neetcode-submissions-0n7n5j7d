class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        U: find two numbers which sum to target
        M: Hash + Subtraction
        P: target - num in hash ? if so return else add num and idx

        """

        seen = defaultdict(int)

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff],i]
            seen[num] = i
        
        return -1