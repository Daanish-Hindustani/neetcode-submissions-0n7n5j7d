class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) ==  1:
            return 0
        
        l,r = 0,1

        max_res = 0
        temp = 0

        while l<=r and r<len(prices):
            temp = prices[r] - prices[l]
            if temp < 0:
                l+=1
                temp = 0
            else:
                max_res = max(max_res, temp)
                r+=1
        
        return max_res