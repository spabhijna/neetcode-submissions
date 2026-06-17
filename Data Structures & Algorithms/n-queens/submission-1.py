class Solution:
    # State: [1,3,0,2] list of already of placed queens
    # Candidates: position in a board
    # Valid Cadidate: position that is not attacked by already placed queens
    # i.e., only one queen in each row, each column and not diagonally adjescent to another queen 
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.solutions = []
        self.col = set()
        self.pos_diag = set()
        self.neg_diag = set()

        self.solve([], n)
        return self.solutions
    
    def solve(self, state, n):
        row = len(state)
        if len(state) == n:
            self.solutions.append(self.build_board(state, n))
        
        for candidate in self.get_candidates(n):
            if candidate in self.col or row + candidate in self.pos_diag or row - candidate in self.neg_diag:
                continue
            
            state.append(candidate)
            self.col.add(candidate)
            self.pos_diag.add(row + candidate)
            self.neg_diag.add(row - candidate)
            self.solve(state, n)

            self.col.remove(candidate)
            self.pos_diag.remove(row + candidate)
            self.neg_diag.remove(row - candidate)
            state.pop()
    
    def build_board(self, state, n):
        board = []
        for col in state:
            string = '.' * col + 'Q' +'.' * (n - col - 1)
            board.append(string)
        return board

    def get_candidates(self, n):
        return range(n)


        