class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = defaultdict(int)
        time = 0
        q = deque()
        heap = []


        for task in tasks:
            freq[task] += 1
        

        for task in freq.values():
            heapq.heappush(heap, -1*task)

        
        while heap or q:
            time += 1
            if heap:
                cnt = heapq.heappop(heap)
                cnt += 1

                # If cnt is 0 we want to ignore and not put back in heap/q
                if cnt:
                    q.append((cnt, time+n))
            
            if q:
                if q[0][1] <= time:
                    heapq.heappush(heap, q.popleft()[0])
        
        return time
