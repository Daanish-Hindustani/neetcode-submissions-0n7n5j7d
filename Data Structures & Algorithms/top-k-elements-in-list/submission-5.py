class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)

        for num in nums:
            cnt[num] += 1
        

        heap = []

        for key, val in cnt.items():
            heapq.heappush(heap, (val, key))

            if len(heap) > k:
                heapq.heappop(heap)
            
        
        res = []

        for i in range(k):
            res.append(heap[i][1])
        
        return res