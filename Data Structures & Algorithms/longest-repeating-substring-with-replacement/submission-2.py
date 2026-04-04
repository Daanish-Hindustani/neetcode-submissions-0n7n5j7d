class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_sub = 0

        freq = defaultdict(int)

        l = 0

        for r in range(len(s)):
            freq[s[r]] += 1

            while (r-l+1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l +=1 
            
            max_sub = max(max_sub, r-l+1)
        
        return max_sub
            

