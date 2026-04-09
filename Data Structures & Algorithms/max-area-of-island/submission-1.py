class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        def dfs(i,j):
            if (i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j]==0):
                return 0
            grid[i][j] = 0
            current_area = (
                1 + dfs(i+1,j) + dfs(i,j+1) + dfs(i-1,j) + dfs(i,j-1)
            )

            return current_area
        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    maxArea = max(maxArea, area)
        
        return maxArea
