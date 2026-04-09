from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        tickets.sort()
        for i, o in tickets:
            graph[i].append(o)
        
        res = ['JFK']

        def dfs(node):
            if len(res) == len(tickets) + 1:
                return True
            if node not in graph:
                return False
            
            temp = list(graph[node])
            for i, v in enumerate(temp):
                graph[node].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                graph[node].insert(i, v)
                res.pop()
            return False
        
        dfs('JFK')
        return res
