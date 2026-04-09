from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        INF = 2**31 - 1
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    grid[nr][nc] == INF):
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr,nc))