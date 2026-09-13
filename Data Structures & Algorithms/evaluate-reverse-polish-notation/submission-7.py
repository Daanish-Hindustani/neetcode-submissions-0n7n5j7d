class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        numbers = ["0","1","2","3","4","5","6","7","8","9"]

        for token in tokens:
            if str(token) in numbers:
                stack.append(token)
            else:
                print(stack)
                number_2 = int(stack.pop())
                number_1 = int(stack.pop())

                if token == '+':
                    stack.append(number_1 + number_2)
                elif token == "-":
                    stack.append(number_1 - number_2)
                elif token == "/":
                    stack.append(number_1 // number_2)
                else:
                    stack.append(number_1 * number_2)
        
        return int(stack[-1])