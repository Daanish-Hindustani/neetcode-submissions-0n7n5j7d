class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        st = []
        res = [0]*len(temperatures)

        for i, t in enumerate(temperatures):
            while st and t > st[-1][0]:
                res[st[-1][1]] = i - st[-1][1]
                st.pop()
            
            st.append((t,i))

        return res
                