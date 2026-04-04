class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        R: Given two strings, find an overlap of chars such that the overlap of s2 is a permutation of s1
        I: We need to use a sliding window of s1 length to find possible solutions, then use a hash to keep count of freq
        D: Sliding window, hash
        A:
            1) Create a hash for s1 and initialize a sliding window on s2
            2) For each window, check if the freq of s1 matches the freq in the current window
            3) If so, return True. Otherwise, slide the window by removing from left and adding from right
        """

        if len(s2) < len(s1):
            return False

        k = len(s1)

        freq_s1 = [0] * 26
        for ch in s1:
            freq_s1[ord(ch) - ord('a')] += 1

        freq_s2 = [0] * 26
        for ch in s2[:k]:
            freq_s2[ord(ch) - ord('a')] += 1

        if freq_s2 == freq_s1:
            return True

        l = 0
        for r in range(k, len(s2)):
            freq_s2[ord(s2[r]) - ord('a')] += 1
            freq_s2[ord(s2[l]) - ord('a')] -= 1
            l += 1

            if freq_s2 == freq_s1:
                return True

        return False
