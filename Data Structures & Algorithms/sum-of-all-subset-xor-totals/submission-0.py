class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.s = 0

        def solve(state, start_idx):
            self.s = self.s + self.xor(state)

            for idx in range(start_idx, len(nums)):
                num = nums[idx]

                state.append(num)
                solve(state, idx+1)
                state.pop()
        solve([], 0)
        return self.s
    
    def xor(self, state):
        a = 0
        for num in state:
            a = a ^ num
        return a
