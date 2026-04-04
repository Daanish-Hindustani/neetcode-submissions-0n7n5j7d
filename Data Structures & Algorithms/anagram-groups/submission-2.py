class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group_freq = defaultdict(list)

        for word in strs:

            temp = [0] * 26

            for char in word:
                idx = ord(char) - ord('a')
                temp[idx] += 1

            group_freq[tuple(temp)].append(word)

        return list(group_freq.values())
            

        

