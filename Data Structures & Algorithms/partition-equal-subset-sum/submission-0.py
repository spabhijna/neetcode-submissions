class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        memo = {}

        def recursion(current_sum,idx):
            if current_sum == target:
                return True
            
            if current_sum > target or idx >= len(nums):
                return False
            
            state = (current_sum, idx)

            if state in memo:
                return memo[state]

            result = recursion(current_sum + nums[idx], idx + 1) or recursion(current_sum, idx + 1)

            memo[state] = result
            return result
        
        return recursion(0, 0)
                
            
        
        