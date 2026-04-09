class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
                return 0

            grid[i][j] = 0 

            
            return (1 + 
                    dfs(i + 1, j) +
                    dfs(i - 1, j) +
                    dfs(i, j + 1) +
                    dfs(i, j - 1))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    current_island_area = dfs(i, j)
                    maxArea = max(maxArea, current_island_area)
        
        return maxArea