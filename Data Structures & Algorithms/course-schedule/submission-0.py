from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)
        
        visited = [False] * numCourses
        stack = [False] * numCourses

        def dfs(node):
            visited[node] = True
            stack[node] = True

            for nei in graph[node]:
                if stack[nei]:
                    return True
                if not visited[nei]:
                    if dfs(nei):
                        return True
            stack[node] = False
            return False
        for node in range(numCourses):
            if not visited[node]:
                if dfs(node):
                    return False
        
        return True
            
            
        
