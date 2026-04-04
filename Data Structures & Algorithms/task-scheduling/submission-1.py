class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Max heap -> freq task (freq)
        # Queue -> keep item that are ideal (freq, time)
        # time 

        freq = defaultdict(int)

        for task in tasks:
            freq[task] += 1
        
        time = 0

        heap = []

        for val in freq.values():
            heapq.heappush(heap, -1*val)
        
        q = deque([])

        while heap or q:
            time += 1

            if heap:
                task_freq = heapq.heappop(heap)
                task_freq += 1
                if task_freq:
                    q.append((task_freq, time + n))
            
            if q and q[0][1] <= time:
                heapq.heappush(heap,q.popleft()[0])

        return time

