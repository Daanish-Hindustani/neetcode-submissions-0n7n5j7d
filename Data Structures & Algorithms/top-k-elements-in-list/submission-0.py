class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        temp = [[] for _ in range(len(nums)+1)]

        for num in nums:
           freq[num] += 1
        
        
        for key,v in freq.items():
           temp[v].append(key)
        
        print(temp)
        counter = 0
        res = []
        for i in range(len(temp)-1, -1, -1):
           for nested_val in temp[i]:
              if k == counter:
                 break
              counter += 1
              res.append(nested_val)
        return res
              
        