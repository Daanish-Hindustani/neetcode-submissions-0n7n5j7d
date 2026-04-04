class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = set()
        
        for num in nums:
            if num in hash_table:
               return True
            hash_table.add(num)
       
        return False