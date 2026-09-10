class Solution:
    def isValid(self, s: str) -> bool:
        vals = {

            "}":"{",
            "]":"[",
            ")":"("
        }


        stack = []

        for char in s:
            if not stack:
                stack.append(char)
            
            elif stack and char in vals:
                popped_val = stack.pop()
                if popped_val != vals[char]:
                    return False
            else:
                stack.append(char)
        
        if stack:
            return False
        
        return True
            