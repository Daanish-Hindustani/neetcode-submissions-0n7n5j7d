class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)

        l = 0

        max_cnt = 0
        for r in range(len(s)):
            
            freq[s[r]] += 1
            while r>=l and r-l+1 - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            
            max_cnt = max(max_cnt, r-l+1)
        
        return max_cnt
            


