class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        print(nums)
        res = []
        for curr in range(len(nums)-2):
            if curr != 0 and nums[curr-1] == nums[curr]:
                continue
            l,r = curr+1, len(nums)-1
      
            while l<r:
                val = nums[curr] + nums[l] + nums[r]
                if val > 0:
                    r-=1
                elif val < 0:
                    l += 1
                else:
                    res.append([nums[curr] , nums[l] , nums[r]])
                    l+=1
                    r-= 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
                    
                    while nums[r] == nums[r+1] and l<r:
                        r-=1
        
        return res

                