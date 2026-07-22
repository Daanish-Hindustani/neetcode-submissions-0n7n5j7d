class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l,r = 0, len(nums) -1

        min_val = float('inf')

        while l<=r:
            mid = (l+r)//2
            min_val = min(nums[mid], nums[l], nums[r])

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid +1
        
        return min_val