class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)

        if total_sum % k != 0:
            return False
        
        target = total_sum // k

        nums.sort(reverse = True)

        if nums[0] > target:
            return False

        bucket = [0] * k

        def backtrack(idx):
            if idx == len(nums):
                return True
            
            for i in range(k):
                if bucket[i] + nums[idx] <= target:
                    bucket[i] = bucket[i] + nums[idx]

                    if backtrack(idx+1):
                        return True

                    bucket[i] = bucket[i] - nums[idx]
                
                if bucket[i] == 0:
                    break
            return False
        if backtrack(0):
            return True
        return False