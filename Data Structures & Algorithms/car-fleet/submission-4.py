class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combine = []
        st = []

        for i in range(len(position)):
            combine.append((position[i], speed[i]))
        
        combine.sort(reverse = True)

        for p,s in combine:
            st.append((target-p)/s)

            while len(st) >= 2 and st[-2] >= st[-1]:
                st.pop()
        

        return len(st)