from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(i, j):
            queue = deque([(i, j)])
            visited.add((i,j))

            while queue:
                r, c = queue.popleft()

                for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                    ni, nj = r + di, c + dj

                    if (0 <= ni < rows and 
                        0 <= nj < cols and 
                        (ni,nj) not in visited and 
                        grid[ni][nj] == '1'):

                        visited.add((ni, nj))
                        queue.append((ni, nj))
        
        no_islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    bfs(i,j)
                    no_islands += 1
        
        return no_islands



