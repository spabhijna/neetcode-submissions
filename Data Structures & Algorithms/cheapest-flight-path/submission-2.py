from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        
        for u, v, w in flights:
            graph[u].append((v, w))
            
        pq = [(0, src, 0)]
        best = {}

        while pq:
            cost, node, stops = heapq.heappop(pq)

            if node == dst:
                return cost
            
            if stops > k:
                continue
            
            for nei, w in graph[node]:
                new_cost = cost + w

                if (nei, stops) not in best or best[(nei, stops)] > new_cost:
                    best[(nei, stops)] = new_cost
                    heapq.heappush(pq, (new_cost, nei, stops+1))
        return -1
        