from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        INF = 2**31 - 1
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def bfs(i, j):
            q = deque([(i,j)])
            visit = [[False] * cols for _ in range(rows)]
            visit[i][j] =True
            steps = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc

                        if (0 <= nr < rows and 0 <= nc < cols and not visit[nr][nc] and grid[nr][nc] != -1):
                            visit[nr][nc] = True
                            q.append((nr, nc))
                        
                steps += 1
            return INF
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
        
                
                    
                         
            
                    
            

        