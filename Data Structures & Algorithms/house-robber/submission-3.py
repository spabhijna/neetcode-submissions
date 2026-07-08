class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        prev2 = nums[0]
        prev1 = max(nums[1], nums[0])

        curr = 0
        for i in range(2, len(nums)):
            curr = max(prev1, nums[i] + prev2)

            prev2 = prev1
            prev1 = curr
        return prev1

        