from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        res = []

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r, c, visited):
            if (r, c) in visited:
                return False, False

            visited.add((r, c))

            pacific = (r == 0 or c == 0)
            atlantic = (r == rows-1 or c == cols-1)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if heights[nr][nc] <= heights[r][c]:
                        p, a = dfs(nr, nc, visited)
                        pacific = pacific or p
                        atlantic = atlantic or a

            return pacific, atlantic


        for r in range(rows):
            for c in range(cols):
                visited = set()
                p, a = dfs(r, c, visited)
                if p and a:
                    res.append([r, c])

        return res