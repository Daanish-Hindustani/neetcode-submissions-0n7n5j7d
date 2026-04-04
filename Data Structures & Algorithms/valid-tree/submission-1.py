class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = [[] for _ in range(n)]
        
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        pred = {0: None}
        cycle = False

        def visit(node):
            nonlocal cycle 
            if cycle:
                return
            for nbr in adj_list[node]:
                if nbr not in pred:
                    pred[nbr] = node
                    visit(nbr)
                elif pred[node] != nbr:
                    cycle = True

        visit(0)
        connected = len(pred) == n
        return not cycle and connected
