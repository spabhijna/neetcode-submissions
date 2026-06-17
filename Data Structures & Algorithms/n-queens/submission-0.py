class Solution:
    # State: [1,3,0,2] list of already of placed queens
    # Candidates: position in a board
    # Valid Cadidate: position that is not attacked by already placed queens
    # i.e., only one queen in each row, each column and not diagonally adjescent to another queen 
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.solutions = []
        self.solve([], n)
        return self.solutions

    def valid_candidate(self, state, n, candidate_col):
        next_row = len(state)

        for r, c in enumerate(state):
            if c == candidate_col:
                return False
            if r + c == next_row + candidate_col:
                return False
            if r - c == next_row - candidate_col:
                return False
            
        return True
    
    def solve(self, state, n):
        if len(state) == n:
            self.solutions.append(self.build_board(state, n))
        
        for candidate in self.get_candidates(n):
            if self.valid_candidate(state, n, candidate):
                state.append(candidate)
                self.solve(state, n)
                state.pop()
    
    def build_board(self, state, n):
        board = []
        for col in state:
            string = '.' * col + 'Q' +'.' * (n - col - 1)
            board.append(string)
        return board

    def get_candidates(self, n):
        return range(n)


        