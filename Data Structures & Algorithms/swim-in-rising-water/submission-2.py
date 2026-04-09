import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = grid[0][0]
        pq = [(grid[0][0], 0, 0)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while pq:
            elev, r, c = heapq.heappop(pq)

            if (r, c) == (rows-1,cols-1):
                return elev
            
            if elev > dist[r][c]:
                continue
            
            for dr, dc in directions:
                nr, nc = r + dr, c+ dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    new_elev = max(elev, grid[nr][nc])
                    if new_elev < dist[nr][nc]:
                        dist[nr][nc] = new_elev
                        heapq.heappush(pq, (new_elev, nr, nc))
        return -1