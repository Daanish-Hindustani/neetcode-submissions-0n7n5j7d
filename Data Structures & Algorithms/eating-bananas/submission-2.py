class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        R: Given some array of number, where each element represents a pile of bannanas, 
        and we are given a total number of hours to eat the bannanas. 
        we need to minimizwe the rate of bannans per hour eatten such 
        that we are at or below the alotted time.
        I: We have a set of values from 1 ... n, 
        and we apply a binary seach which adjusts k to the min value.
        We dictate the left or right sub section based on the total hour utalized with chossen k
        D: BS + Adjust k based on result of chossen k + return optimal value
        E:
            1) we create an array between 1 ... max(piles)
            2) Preform a BS to find a k value
            3) Iterate through the list and result total hours
            4) adjust k value via bs if value is to big or to small
            5) Repeat till r<l

        """

        
        def BS(l, r):
            if r < l:
                return l

            k = (l + r) // 2

            res_hr = 0
            for p in piles:
                res_hr += math.ceil(p / k)

            if res_hr <= h:
                return BS(l, k - 1)  # try smaller k
            else:
                return BS(k + 1, r)  # try bigger k
        
        return BS(1, max(piles))






