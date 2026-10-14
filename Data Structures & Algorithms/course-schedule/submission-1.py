class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}

        visited = set()

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
           

        
        def dfs(crs):
            if crs in visited:
                return False

          

            visited.add(crs)

            for nei in pre_map[crs]:
                if not dfs(nei):
                    return False
            
            visited.remove(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True

            
