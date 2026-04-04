class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq = defaultdict(list)

        for word in strs:
            curr_freq = [0]*26

            for char in word:
                idx = ord(char) - ord("a")
                curr_freq[idx] += 1
            
            curr_freq = tuple(curr_freq)

            freq[curr_freq].append(word)
        

        return list(freq.values())
