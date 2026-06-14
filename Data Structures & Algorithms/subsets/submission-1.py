class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        powerset = []
        subset = []

        def backtrack(start):
            powerset.append(list(subset))

            for i in range(start, len(nums)):
                subset.append(nums[i])
                # FIX: Pass the next index (i + 1), not the value nums[i]
                backtrack(i + 1)
                subset.pop()
        
        backtrack(0)
        return powerset