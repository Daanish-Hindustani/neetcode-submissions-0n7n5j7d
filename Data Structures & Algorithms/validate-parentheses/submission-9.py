class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        st = []

        for char in s:
            
            if char in mapping and st and st[-1] == mapping[char]:
                st.pop()
            elif s not in mapping:
                st.append(char)
            else:
                return False
        

        return True if not st else False
