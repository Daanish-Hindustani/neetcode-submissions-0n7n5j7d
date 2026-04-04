class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        heap = []
        q = deque([])
        time = 0
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1
        
        for task in freq.values():
            heapq.heappush(heap, -1*task)
        
        while heap or q:
            time += 1

            if heap:
                cnt = heapq.heappop(heap)
                cnt += 1     
                if cnt:   
                    q.append((cnt, time+n))
            
            if q:
                if q[0][1] <= time:
                    heapq.heappush(heap, q.popleft()[0])
        
        return time

