class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        freq_t = defaultdict(int)

        for char in t:
            freq_t[char] += 1

        l = 0
        num_comp = len(freq_t)
        max_curr = ""
        max_num = float('inf')
        freq_s = defaultdict(int)

        cnt = 0

        for r in range(len(s)):
            
            freq_s[s[r]] += 1

            if freq_s[s[r]] == freq_t[s[r]]:
                cnt += 1
            
            while cnt == num_comp  and l<=r:
                if max_num >= r-l+1:
                    max_num = r-l+1
                    max_curr = s[l:r+1]

                freq_s[s[l]] -= 1

                if freq_s[s[l]] < freq_t[s[l]]:
                    cnt -= 1
                
                l +=1
        
        return max_curr

             
