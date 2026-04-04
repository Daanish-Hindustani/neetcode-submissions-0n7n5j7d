class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        U: Given a rotated array, find the the min val
        M: BS
        P: given a mid val, compare with the edges
        if the r>mid go left
        if the mid < r go right
        else return mid
        """

        l,r = 0, len(nums)-1

        while l<r:
            mid = (l+r) // 2

            if nums[mid] < nums[r]:
                r = mid
            
            else:
                l = mid + 1
        
        return nums[l]
            
