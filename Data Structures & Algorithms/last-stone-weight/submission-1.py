class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)*-1
            stone2 = heapq.heappop(stones)*-1

            if stone1 == stone2:
                continue
            
            heapq.heappush(stones, abs(stone1-stone2)*-1)
        
        if not stones:
            return 0
        
        return stones[0]*-1