class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        nums.sort()
        n = len(nums)
        visited = [False for _ in range(n)]
        def solve(state):
            if len(state) == n:
                solutions.append(state[:])
                return
            for idx in range(n):
                if visited[idx]:
                    continue

                if idx > 0 and nums[idx] == nums[idx - 1] and not visited[idx - 1]:
                    continue
                num = nums[idx]

                visited[idx] = True
                state.append(num)
                solve(state)
                visited[idx] = False
                state.pop()
        solve([])
        return solutions
        