class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)

        if total_sum % k != 0:
            return False
        
        target = total_sum // k

        nums.sort(reverse = True)

        if nums[0] > target:
            return False

        visited = [False for _ in range(len(nums))]

        def backtrack(bucket_idx, current_sum, start_idx):
            if bucket_idx == k - 1:
                return True
            
            if current_sum == target:
                return backtrack(bucket_idx + 1, 0, 0)

            for i in range(start_idx, len(nums)):
                if visited[i]:
                    continue

                if current_sum + nums[i] <= target:
                    current_sum += nums[i]

                    visited[i] = True
                    if backtrack(bucket_idx, current_sum, i+1):
                        return True

                    current_sum -= nums[i]
                    visited[i] = False
            return False

        if backtrack(0, 0, 0):
            return True
        return False