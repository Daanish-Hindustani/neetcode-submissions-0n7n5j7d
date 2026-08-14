class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ana_dict = defaultdict(int)
        for char in s:
            ana_dict[char] += 1
        

        for char in t:
            if char not in ana_dict:
                return False
            
            ana_dict[char] -=1 
        
        for k,v in ana_dict.items():
            if v != 0:
                return False
        
        return True
