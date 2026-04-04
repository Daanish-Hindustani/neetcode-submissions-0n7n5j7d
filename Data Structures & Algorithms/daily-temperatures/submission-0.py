class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        R: Given an array of daily temperatures, return a list where each element tells how many days
           to wait until a warmer temperature. If there's no future day, return 0.
        I: Brute force is O(n^2). We can optimize using a monotonic decreasing stack (stores indices).
        D: Stack
        E: 
            1) Iterate over each day and temperature
            2) Maintain a stack of indices of previous days with decreasing temperatures
            3) When current temperature is greater than temperature at index on top of stack:
               - pop and update result with day difference
        """

        res = [0] * len(temperatures)
        stack = []  # Will store pairs: (temperature, index)

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prev_temp, prev_idx = stack.pop()
                res[prev_idx] = idx - prev_idx
            stack.append((temp, idx))

        return res