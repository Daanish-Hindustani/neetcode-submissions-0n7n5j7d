class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_s = defaultdict(int)

        for char in s:
            freq_s[char] += 1
        
        for char in t:
            if freq_s[char] == 0:
                return False
            freq_s[char] -=1
        
        if len(set(list(freq_s.values()))) != 1 and 0 not in set(freq_s.values()):
            return False

        return True
