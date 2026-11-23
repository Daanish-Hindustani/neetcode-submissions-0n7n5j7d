class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        heap = nums
        
        while len(heap) > k:
            heapq.heappop(heap)
        
        return heapq.heappop(heap)