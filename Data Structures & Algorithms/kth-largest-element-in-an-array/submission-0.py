class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] * -1

        heapq.heapify(nums)

        res = 0
        while k > 0:
            res = heapq.heappop(nums) * -1
            k -=1
        
        return res

