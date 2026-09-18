class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        def simulate(k):
            total_hrs = 0
            for pile in piles:
                total_hrs += math.ceil(pile/k)

            return total_hrs


        l,r = 1, max(piles)
        while l<r:
            k = (l+r)//2
            total_hrs = simulate(k)

            if total_hrs > h:
                l = k + 1
            else:
                r = k
                
            
        
        return l


