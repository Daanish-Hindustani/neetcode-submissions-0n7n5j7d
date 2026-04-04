class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        id = 0
        adj_list = [[] for _ in range(n)]
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)


        cc = {}

        def DFS(node, id):
            if node in cc:
                return 
            cc[node] = id
            for nbr in adj_list[node]:
                DFS(nbr, id)
     
        for node in range(n):
            if node not in cc:
                DFS(node, id)
                id += 1
        
        seen = set()
        for v in cc.values():
            seen.add(v)

        return len(seen)
        