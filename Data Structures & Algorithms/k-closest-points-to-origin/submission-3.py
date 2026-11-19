class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points:
            heapq.heappush(heap, (-1*math.dist([x,y], [0,0]), x,y))

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        while heap:
            _, x, y = heapq.heappop(heap)
            res.append([x,y])
        
        return res
            