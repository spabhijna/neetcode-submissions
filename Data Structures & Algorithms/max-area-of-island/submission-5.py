class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(i,j):
            q = deque()
            grid[i][j] = 0
            q.append((i,j))
            res = 1

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc

                    if (nr < 0 or nr >= rows or
                        nc < 0 or nc >= cols or 
                        grid[nr][nc] == 0):
                        continue

                    res += 1
                    q.append((nr,nc))
                    grid[nr][nc] = 0
            return res

        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = bfs(i,j)
                    maxArea = max(maxArea, area)
        
        return maxArea
