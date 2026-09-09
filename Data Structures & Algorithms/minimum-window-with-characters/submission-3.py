class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        sub_t = defaultdict(int)
        sub_s = defaultdict(int)
        cnt = ""

        for char in t:
            sub_t[char] += 1
        
        l = 0

        def check():
            for k,v in sub_t.items():
                if k not in sub_s:
                    return False
                elif sub_s[k] < v:
                    return False
            
            return True


        for r in range(len(s)):
            sub_s[s[r]] += 1

            while check():
                if cnt == "":
                    cnt = s[l:r+1]

                elif r-l+1 < len(cnt):
                    cnt = s[l:r+1]
                sub_s[s[l]] -= 1
                l += 1
            
        
        return cnt
            





