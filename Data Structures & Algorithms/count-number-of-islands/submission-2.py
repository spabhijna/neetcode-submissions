from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def bfs(r, c):
            queue = deque()
            grid[r][c] = '0'
            queue.append((r,c))

            while queue:
                i, j = queue.popleft()

                for di, dj in directions:
                    ni, nj = i + di, j + dj

                    if (ni < 0 or ni >= rows or
                        nj < 0 or nj >= cols or
                        grid[ni][nj] == '0'):
                        continue
                    
                    queue.append((ni, nj))
                    grid[ni][nj] = '0'
            
        
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    bfs(i,j)
        
        return islands
        


