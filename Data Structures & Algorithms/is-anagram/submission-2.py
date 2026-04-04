class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """ 
        U: Check if two strings are anagrams
        M: Dict + traversal
        P: Traverse both lists then check if the dict is empty at the end

        """

        freq = defaultdict(int)
        if len(s) != len(t):
            return False
        
        for ch in s:
            freq[ch] += 1
        
        for ch in t:
            freq[ch] -= 1
        
        for val in freq.values():
            if val != 0:
                return False
        
        return True