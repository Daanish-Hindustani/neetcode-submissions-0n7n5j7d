"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        """
        U: Given an adj list create a deep copy
        M: DFS to iterate through all the copy dict to hold nightbors
        """
        clone = {}
        def dfs(node):
            if node in clone:
                return clone[node]
            
            if not node:
                return
            
            new_node = Node(node.val)
            clone[node] = new_node

            for nigh in node.neighbors:
                new_node.neighbors.append(dfs(nigh))    
            
            return new_node
        
        return dfs(node)