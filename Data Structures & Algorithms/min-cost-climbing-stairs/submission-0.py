class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}

        def DP(i):
            if i >=len(cost):
                return 0
            
            if i in memo:
                return memo[i]
            
            else:
                memo[i] = cost[i] + min(DP(i+1), DP(i+2))
                return memo[i]
        
        return min(DP(0), DP(1))