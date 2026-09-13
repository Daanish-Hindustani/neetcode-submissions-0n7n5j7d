class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
    
        def is_number(s):
            try:
                int(s)
                return True
            except ValueError:
                return False

        for token in tokens:
            
            if is_number(token):
                stack.append(token)
            else:
                number_2 = int(stack.pop())
                number_1 = int(stack.pop())

                if token == '+':
                    stack.append(number_1 + number_2)
                elif token == "-":
                    stack.append(number_1 - number_2)
                elif token == "/":
                    stack.append( number_1 / number_2)
                else:
                    stack.append(number_1 * number_2)

        return int(stack[-1])