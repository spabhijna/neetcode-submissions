from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((v, t))
        
        pq = [(0,k)] 

        distances = {i: float('inf') for i in range(1, n+1)}        
        distances[k] = 0
        while pq:
            distance, node = heapq.heappop(pq)

            if distance > distances[node]:
                continue
            
            for nei, w in graph[node]:
                new_dist = distance + w
                if new_dist < distances[nei]:
                    distances[nei] = new_dist
                    heapq.heappush(pq, (new_dist, nei))
        
        max_time = max(distances.values())
        return max_time if max_time != float('inf') else -1
