class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1] * (n+1)
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return False
        
        elif px != py:
            if self.size[py] > self.size[px]:
                self.size[py] += self.size[px]
                self.parent[px] = py
            else:
                self.size[px] += self.size[py]
                self.parent[py] = px
        
            return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (0,1), (-1, 0), (0, -1)]
        dsu = DSU(ROWS * COLS + 1)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] != 'O':
                    continue
                if (i == 0 or j == 0 or i == ROWS-1 or j == COLS-1):
                    dsu.union(ROWS * COLS, i * COLS + j)
                else:
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if board[ni][nj] == 'O':
                            dsu.union(i * COLS + j, ni * COLS + nj)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    if not dsu.connected(i * COLS + j, ROWS * COLS):
                        board[i][j] = 'X'

        