class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_a = [0] * 26
        freq_b = [0] * 26

        for char in s1:
            freq_a[ord(char) - ord('a')] += 1

        
        l = 0
        for r in range(len(s2)):
            freq_b[ord(s2[r]) - ord('a')] += 1

            if r-l +1 == len(s1):
                if freq_b == freq_a:
                    return True
                
                freq_b[ord(s2[l]) - ord('a')] -= 1
                l += 1
        

        return False
