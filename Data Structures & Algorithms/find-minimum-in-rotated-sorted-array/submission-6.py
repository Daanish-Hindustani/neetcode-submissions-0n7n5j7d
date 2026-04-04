class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        min_val = float('inf')

        l,r = 0, len(nums)-1

        while l<=r:
            mid = (l+r) //2

            min_val = min(nums[mid], nums[l], nums[r])

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid+1

        return min_val

