class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        R: Given a sorted and rotated array along with a target val, find the idx that is assoiated with that target in the rotated array
        I: We will need to use binary search and find a sequence of ordered numbers where the target is
        D: Binary search, if l<mid but target > mid, then l = mid +1,
            if mid >left and target >mid then l = mid +1
            else: mid < right and mid > tagert then r = mid -1
            else: mid > right and mid > target -> l = mid +1
        E:
            

        """
        def bs(l,r):
            if r<l:
                return -1
            
            mid = (l+r) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            
            if nums[l]<=nums[mid]:
                if nums[l]<=target < nums[mid]:
                    return bs(l, mid-1)
                else:
                    return bs(mid+1, r)
            else:
                if nums[mid] < target <= nums[r]:
                    return bs(mid+1, r)
                else:
                    return bs(l, mid-1)
        

        return bs(0,len(nums)-1)