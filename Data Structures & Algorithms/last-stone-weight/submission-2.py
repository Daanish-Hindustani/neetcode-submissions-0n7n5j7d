class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
 
        while len(heap) > 1:
            val1 = -1 * heapq.heappop(heap)
            val2 = -1 * heapq.heappop(heap)

            if val1 == val2:
                continue
            
            elif val2 < val1:
                heapq.heappush(heap, -1*(val1-val2))
            
        
        if len(heap) == 1:
            return -1 * heapq.heappop(heap)
        else:
            return None

