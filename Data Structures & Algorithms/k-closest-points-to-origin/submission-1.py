class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []

        for x,y in points:

            euc = math.sqrt((0-x)**2 + (0-y)**2)
            heapq.heappush(heap, (-1*euc,[x,y]))
            print(heap)
            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []

        for _ in range(len(heap)):
            res.append(heapq.heappop(heap)[1])
        
        return res