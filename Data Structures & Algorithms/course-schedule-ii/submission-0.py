from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)
        
        visited = [False] * numCourses
        stack = [False] * numCourses
        order = []
        def dfs(node):
            stack[node] = True
            visited[node] = True

            for nei in graph[node]:
                if stack[nei]:
                    return False
                if not visited[nei]:
                    if not dfs(nei):
                        return False
            
            order.append(node)
            stack[node] = False
            return True
        for node in range(numCourses):
            if not visited[node]:
                if not dfs(node):
                    return []
        
        return order[::-1]