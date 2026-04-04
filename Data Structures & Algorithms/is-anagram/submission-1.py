class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = defaultdict(int)
        
        if len(s) != len(t):
           return False
     
        for ch in s:
            freq[ch] += 1
        
        for ch in t:
            if ch not in freq:
               return False
            
            elif freq[ch] == 0:
               return False
           
            else: 
               freq[ch] -= 1
           

        for val in freq.values():
            if val != 0:
               return False

        return True
