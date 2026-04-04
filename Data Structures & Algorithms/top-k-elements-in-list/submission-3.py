class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []

        int_freq = defaultdict(int)
        for num in nums:
            int_freq[num] += 1
        
        for key,val in int_freq.items():
            heapq.heappush(heap,[val, key])
            if len(heap) > k:
                heapq.heappop(heap)
            print(heap)
            
        res = []
        while heap:
            _, found_key = heapq.heappop(heap)
            res.append(found_key)
        
        return res

