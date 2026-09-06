class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        cnt = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])

            cnt = max(cnt, r-l+1)
    
        return cnt
