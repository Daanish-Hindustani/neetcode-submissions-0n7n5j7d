class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        processed = ""

        for char in s:
            if not char.isalnum():
                continue
            
            if char.isdigit():
                processed+= char

            processed += char.lower()
        
        return processed == processed[::-1]
