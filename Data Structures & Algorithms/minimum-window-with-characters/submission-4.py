class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        freq_t = defaultdict(int)
        freq_s = defaultdict(int)

        for char in t:
            freq_t[char] += 1
        

        l = 0
        res = ""
        def is_substring():
            for k,v in freq_t.items():
                if freq_s[k] < v:
                    return False
            return True

        for r in range(len(s)):
            freq_s[s[r]] += 1

            while is_substring():
                if res == "":
                    res = s[l:r+1]
                else:
                    if r-l+1 < len(res):
                        res = s[l:r+1]
                
                freq_s[s[l]] -= 1
                l += 1
        
        return res
                


