class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def dp(i):
            if i >= len(cost):
                return 0
            
            res = min((cost[i] + dp(i+1)), (cost[i] + dp(i+2)))
            return res
        
        return min(dp(0), dp(1))