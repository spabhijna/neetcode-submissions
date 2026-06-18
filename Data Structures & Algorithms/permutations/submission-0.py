class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        solutions = []

        def solve(state):
            if len(state) == len(nums):
                solutions.append(state[:])
            
            for num in nums:
                if num not in state:
                    state.append(num)
                    solve(state)
                    state.pop()
                
        solve([])
        return solutions
        