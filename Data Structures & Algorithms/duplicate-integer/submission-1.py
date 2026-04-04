class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        U: Check if there are duplicate numbers in the array
        M: Hash + traversal
        P: Use a hash and traverse the list and check for duplicates
        """

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False