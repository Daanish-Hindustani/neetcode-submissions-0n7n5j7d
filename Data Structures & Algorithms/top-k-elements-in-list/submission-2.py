class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        element_freq = defaultdict(int)

        for num in nums:
            element_freq[num] += 1
        

        max_freq = max(list(element_freq.values()))

        list_freq = [[] for _ in range(max_freq+1)]

        for key,v in element_freq.items():
            list_freq[v].append(key)
        
        res = []

        for i in range(len(list_freq)-1,-1,-1):
            if list_freq[i]:
                sub_list = list_freq[i]

                for val in sub_list:
                    res.append(val)
                    k-=1
                    if k == 0:
                        return res
        
        return res
        
