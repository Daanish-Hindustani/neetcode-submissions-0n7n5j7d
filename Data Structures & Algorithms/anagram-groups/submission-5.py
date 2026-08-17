class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)


        for word in strs:
            cnt = [0]*26
            for char in word:
                cnt[ord(char) - ord('a')] += 1
            
            groups[tuple(cnt)].append(word)
        
        res = []

        for val in groups.values():
            res.append(val)
        
        return res