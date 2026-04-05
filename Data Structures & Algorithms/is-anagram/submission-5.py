class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = defaultdict(int)
        

        for char in s:
            dict_s[char] += 1
        
        for char in t:
            dict_s[char] -= 1
            if dict_s[char] <0:
                return False
        
        for k,v in dict_s.items():
            if v != 0:
                return False
        
        return True
