class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        currentSum = 0
        min_length = float('inf')

        for r in range(len(nums)):
            currentSum += nums[r]

            while currentSum >= target:
                min_length = min(min_length, r - l + 1)
                currentSum -= nums[l]
                l += 1
        
        return min_length if min_length != float('inf') else 0
        
        

