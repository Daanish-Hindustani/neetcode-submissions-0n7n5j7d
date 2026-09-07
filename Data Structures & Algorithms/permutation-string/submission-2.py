class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = [0]*26

        s2_freq = [0]*26

        for char in s1:
            s1_freq[ord(char) - ord('a')] += 1
        

        l = 0

        for r in range(len(s2)):
            s2_freq[ord(s2[r]) - ord('a')] += 1

            if r-l +1 == len(s1):
                if s1_freq == s2_freq:
                    return True

                s2_freq[ord(s2[l]) - ord('a')] -= 1
                l += 1
        
        return False

