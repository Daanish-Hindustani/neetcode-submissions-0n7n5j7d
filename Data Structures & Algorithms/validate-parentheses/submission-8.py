class Solution:
    def isValid(self, s: str) -> bool:
        
        association = {
            "}":"{",
            "]": "[",
            ")":"("
        }

        stack = []

        for char in s:
            if char not in association:
                stack.append(char)
                continue
            
            if not stack:
                return False
            
            if stack.pop() != association[char]:
                return False
            
        
        return True if not stack else False