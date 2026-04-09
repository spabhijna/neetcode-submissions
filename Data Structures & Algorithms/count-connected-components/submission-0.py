from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        visited = set()
        for u, v in edges:
            d[u].append(v)
            d[v].append(u)
        
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for n in d[node]:
                dfs(n)
        
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        
        return res
            


        

        