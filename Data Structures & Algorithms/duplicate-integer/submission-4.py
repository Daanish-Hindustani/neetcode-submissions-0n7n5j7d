class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        """ 
        - Given nums check for duplicates
        - Iterate through the array and caputre numbers and easily check for duplicates
        """

        cache = set()

        for num in nums:
            if num in cache:
                return True
            
            cache.add(num)
        
        return False