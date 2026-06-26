class Solution:
    def trap(self, heights: List[int]) -> int:
        """
        - Keep a montonic decreasing stack 
        - If a height makes it invidalid, pop and get aread between values
        - Add to stack if valid
        """

        st = []
        total = 0
        for i,height in enumerate(heights):
            
            while st and height > heights[st[-1]]:
                top = st.pop()
                if not st:
                    continue

                length = i - st[-1] -1

                area = length * (min(heights[st[-1]], heights[i]) - heights[top])
                total += area

            
            st.append(i)
        
        return total


