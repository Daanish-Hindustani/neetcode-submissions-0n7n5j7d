class Solution:
    def trap(self, heights: List[int]) -> int:
        stk = []
        total = 0

        for i, height in enumerate(heights):
            while stk and height > heights[stk[-1]]:
                top = stk.pop()

                if not stk:
                    continue
                
                length = i - stk[-1] -1

                area = length*(min(heights[stk[-1]], heights[i])- heights[top]) 

                total += area
            
            stk.append(i)
        
        return total

