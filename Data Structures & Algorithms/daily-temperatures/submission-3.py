class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            if stack == []:
                stack.append((temp, i))
            else:
                while stack and temp > stack[-1][0]:
                    top, idx = stack.pop()
                    res[idx] = i - idx
                
                stack.append((temp, i))
        
        return res