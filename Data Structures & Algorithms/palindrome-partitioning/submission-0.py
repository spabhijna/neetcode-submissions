class Solution:
    def partition(self, s: str) -> List[List[str]]:
        solutions = []

        def solve(state, start_idx):
            if start_idx == len(s):
                solutions.append(state[:])
                return
            for candidate_idx in range(start_idx, len(s)):
                candidate = s[start_idx: candidate_idx + 1]
                if candidate[::-1] == candidate:
                    state.append(candidate)
                    solve(state, candidate_idx+1)
                    state.pop()
        
        solve([],0)
        return solutions
        