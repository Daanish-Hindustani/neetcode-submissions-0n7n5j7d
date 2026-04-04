class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = [[] for _ in range(len(nums)+1)]
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        for id,v in freq.items():
            freq_list[v].append(id)

        
        res = []
        print(freq_list)
        for i in range(len(freq_list)-1,-1,-1):
            print(len(res), k)
            if len(res) == k:
                print("ji")
                return res
            
            for num in freq_list[i]:
                res.append(num)
        
        return res
            
        
