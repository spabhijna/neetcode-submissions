class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        def linear_rob(start, end):
            prev2 = nums[start]
            prev1 = max(nums[start], nums[start + 1])
            
            for i in range(start + 2, end + 1):
                curr = max(prev1, nums[i] + prev2)
                prev2 = prev1
                prev1 = curr
            return prev1

        return max(linear_rob(0, len(nums) - 2), linear_rob(1, len(nums) - 1))