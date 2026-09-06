class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)

        l = 0
        cnt = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            while (r-l+1) - max(list(freq.values())) > k:
                freq[s[l]] -= 1
                l += 1
            
            cnt = max(cnt, r-l+1)
            
        
        return cnt