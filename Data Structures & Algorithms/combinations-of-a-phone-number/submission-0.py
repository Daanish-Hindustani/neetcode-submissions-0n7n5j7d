class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if digits == "":
            return res
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        digits = list(digits)
        sol = []

        def visit(n):
            if n == len(digits):
                res.append("".join(sol[:]))
                return
            
            choices = digitToChar.get(digits[n])

            for choice in choices:
                sol.append(choice)
                visit(n+1)
                sol.pop()
        visit(0)
        return res