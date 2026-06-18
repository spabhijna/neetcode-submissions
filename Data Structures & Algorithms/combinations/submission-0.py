class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        solutions = []

        def backtrack(state, start_idx):
            if len(state) == k:
                solutions.append(state[:])
                return 
            
            for i in range(start_idx, n+1):

                state.append(i)
                backtrack(state, i+1)
                state.pop()
        
        backtrack([], 1)
        return solutions

        