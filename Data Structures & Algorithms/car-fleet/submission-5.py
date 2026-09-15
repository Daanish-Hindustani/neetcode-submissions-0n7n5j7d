class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # given cars at a position and speed we need to find groups of cars that reach target
        # Note single lane road no passing


        combine = []
        st = []

        for i in range(len(position)):
            combine.append((position[i], speed[i]))
        
        combine.sort(reverse=True)

        for p,s in combine:
            st.append((target - p)/s)
            if len(st) >= 2 and st[-2] >= st[-1]:
                st.pop()
        
        return len(st)

