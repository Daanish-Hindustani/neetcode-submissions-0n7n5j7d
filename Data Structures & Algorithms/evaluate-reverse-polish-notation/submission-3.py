class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        R: Given a string of tokens create a valid arametic expression abnd return the sum
        I: We need to use a stack to pop off value and find aritmentic expressions
        D: Use a stack
        E: 
            1) pop from the stack
            2) if the value is a arit. we need to add the last to vals and add to the end of the stack
            3) at the end we will have on val
        """
        stack = []

        for i in range(len(tokens)):
            if tokens[i] == "+":
                val = int(stack.pop()) + int(stack.pop())
                stack.append(val)
            elif tokens[i] == "-":
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                val = int(val2 - val1)
                stack.append(val)
            elif tokens[i] == "*":
                val = int(stack.pop()) * int(stack.pop())
                stack.append(val)
            elif tokens[i] == "/":
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                val = int(val2 / val1)
                stack.append(val)
            else:
                stack.append(int(tokens[i]))
        
        return stack[0]

            