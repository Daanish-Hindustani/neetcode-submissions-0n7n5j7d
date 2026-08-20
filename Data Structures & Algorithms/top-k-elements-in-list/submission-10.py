class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        
        heap = []

        for key, value in freq.items():
            heapq.heappush(heap, (value, key))

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for _, element in heap:
            res.append(element)
        
        return res
                