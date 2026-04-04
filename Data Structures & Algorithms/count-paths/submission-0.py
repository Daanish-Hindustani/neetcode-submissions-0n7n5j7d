class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Count the number of unique paths from top-left to bottom-right in an m x n grid.
        Only moves allowed: right or down.
        """
        cache = {}
        
        def dp(x, y):
            # If we reached the destination → one valid path
            if (x, y) == (m-1, n-1):
                return 1
            
            # If out of bounds → no path
            if x >= m or y >= n:
                return 0
            
            if (x, y) in cache:
                return cache[(x, y)]
            
            # Explore right and down
            res = dp(x+1, y) + dp(x, y+1)
            cache[(x, y)] = res
            return res
        
        return dp(0, 0)