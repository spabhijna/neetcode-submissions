from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootx = find(x)
            rooty = find(y)

            if rootx != rooty:
                parent[rooty] = rootx
            else:
                return True
            return False
        
        for u, v in edges:
            if union(u, v):
                return [u, v]
        
        return []
            
        
