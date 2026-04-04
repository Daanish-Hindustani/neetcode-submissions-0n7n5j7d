class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for string in strs:
            freq = [0] * 26
            for ch in string:
                freq[ord(ch) - ord('a')] += 1
            
            anagram_dict[tuple(freq)].append(string)
        
        return list(anagram_dict.values())
