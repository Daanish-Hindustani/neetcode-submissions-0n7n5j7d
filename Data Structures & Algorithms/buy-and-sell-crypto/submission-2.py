class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 0
        profits = 0

        for r in range(len(prices)):

            while prices[r] - prices[l] < 0 and r>l:
                l += 1

            profits = max(profits, prices[r] - prices[l])

            r+=1

        return profits

            
