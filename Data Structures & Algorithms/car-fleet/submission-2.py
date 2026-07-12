class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []
        st = []
        for i in range(len(position)):
            combined.append((position[i],speed[i]))
        
        combined.sort(reverse = True)

        for p, s in combined:
            
            st.append((target-p)/s)

            if len(st) >= 2 and st[-2] >= st[-1]:
                st.pop()
            
        return len(st)

