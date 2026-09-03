class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1

        max_total = 0

        while r < len(prices):

            if prices[r] >= prices[l]:
                max_total = max(max_total, prices[r]-prices[l])
                r += 1
            else:
                l += 1
        
        return max_total