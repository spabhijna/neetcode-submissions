from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        tickets.sort(reverse=True)
        for i, o in tickets:
            graph[i].append(o)
        
        res = []

        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            res.append(node)
        
        dfs('JFK')
        return res[::-1]
