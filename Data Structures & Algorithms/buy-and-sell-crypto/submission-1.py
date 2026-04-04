class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        l,r = 0, 1

        while l<r and r < len(prices):
            profit = prices[r] - prices[l]
            print(r,l, profit)
            max_profit = max(max_profit, profit)

            if profit < 0:
                l = r
            
            
            r+= 1
        
        return max_profit
            