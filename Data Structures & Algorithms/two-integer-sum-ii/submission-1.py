class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(l, r, tar, avoid):
            if l > r:
                return None
            mid = (l + r) // 2
            if nums[mid] == tar and mid!=avoid:
                return mid
            elif nums[mid] > tar:
                return binarySearch(l, mid - 1, tar, avoid)
            else:
                return binarySearch(mid + 1, r, tar, avoid)
        
        for i,num in enumerate(nums):
            val = target-num 
            res = binarySearch(i,len(nums)-1, val, i)
            if res == None:
                continue
            
            return [i+1,res+1]
            