from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        src = []
        fresh = 0
        time = 0
        visited = set()
        q = deque()
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if(0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            time += 1
        return time if fresh == 0 else -1





        