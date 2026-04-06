class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """ 
        G: given nums and k, find the k most freq elements

        1. sort the array
        2. Group numbers based on freq
        3. extract top k

        Complexity:
            time - nlogn + o(n) + o(k) -> O(nlogn)
            time - nlogk
            space: O(n) -> O(n) + O(k)


        """

        cnt = defaultdict(int)

        # Get cnt of nums
        for num in nums:
            cnt[num] += 1
                
        # Append freq values to heap
        heap = []

        for key,v in cnt.items():
            heapq.heappush(heap, (v, key))
        
            if len(heap) > k:
                heapq.heappop(heap)

        print(heap)
        # get results of values
        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
        
        
