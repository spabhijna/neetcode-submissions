class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        res = []
        pacific = set()
        atlantic = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(i,j, visited):
            visited.add((i, j))

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (0 <= ni < rows and
                    0 <= nj < cols and
                    (ni, nj) not in visited and
                    heights[ni][nj] >= heights[i][j]):
                    dfs(ni,nj, visited)
        for c in range(cols):
            dfs(0,c,pacific)
            dfs(rows-1,c,atlantic)
        for r in range(rows):
            dfs(r,0,pacific)
            dfs(r,cols-1, atlantic)
        
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])
        
        return res