class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        minR = 0
        
        for i in range(len(nums)):
            if nums[i] - 1 not in d:
                res = 1
                t = nums[i]
                while t+1 in d:
                    t += 1
                    res += 1
                minR = max(minR, res)
        
        return minR 


        
        
               
            
        
        