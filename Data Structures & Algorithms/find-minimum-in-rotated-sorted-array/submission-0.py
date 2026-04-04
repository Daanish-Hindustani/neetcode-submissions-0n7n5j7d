class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        R: Given an array that has been rotated X number of times, return the most min val
        I: Use binary search, compare mid with left and right, if mid < right then we can return 
            right else if if mid > right we adjut the right ptr and search the left subsection
        D: Binary Search comparing left and right ptrs
        E:
            1) Create a BS algo
            2) In the algo chech if mid < right right = mid -1
            3) if mid>right -> left = mid +1
            4) at the end we have the most min val
        """

        def bs(l,r):   
            if r==l:
                return nums[l]
            
            mid = (l+r) //2
            print(nums[mid])
            if nums[mid] > nums[r]:
               
                return bs(mid+1, r)
            else:
                return bs(l, mid)

        
        return bs(0,len(nums)-1)