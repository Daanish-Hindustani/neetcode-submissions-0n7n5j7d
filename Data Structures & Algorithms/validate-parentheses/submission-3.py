class Solution:
    def isValid(self, s: str) -> bool:
        """
        R: Given a string s we need to validate symetric pattern of chars
        I: We should use a stack and pop and check and add
        D: Stack + validation check
        E: 
            1) Create a stack and a dict of vals(keep track of pairs)
            2) For each value of the opening pair we add to the stack
            3) For each closing value we remove from the stack and check of its pair together via a dict
            4) Return True if stack is empty at end else Flase if there is a miss match 
        """

        stack = []

        look_up = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        for ch in s:
            if ch not in look_up.keys():
                stack.append(ch)
            else:
                if stack == [] or stack.pop() != look_up[ch]:
                    return False
                
        return True if stack == [] else False
        