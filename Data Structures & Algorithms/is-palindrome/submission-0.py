class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = []

        for ch in s:
            if ch != " " and ch.isalnum():
                filtered.append(ch.lower())
        
        print(filtered)
        if filtered == filtered[::-1]:
            return True
        
        return False