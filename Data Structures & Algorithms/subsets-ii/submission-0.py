class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        nums.sort()

        def solve(state, start_idx):
            solutions.append(state[:])

            for candidate_idx in range(start_idx, len(nums)):
                num = nums[candidate_idx]
                if candidate_idx > start_idx and nums[candidate_idx] == nums[candidate_idx - 1]:
                    continue
                state.append(num)
                solve(state, candidate_idx+1)
                state.pop()
        solve([], 0)
        return solutions