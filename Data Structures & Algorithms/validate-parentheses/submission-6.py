class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        stack = []

        for ch in s:
            if ch in mapping:
                if not stack:
                    return False

                val = stack.pop()
                if val != mapping[ch]:
                    return False
            else:
                stack.append(ch)
        
        return True if not stack else False