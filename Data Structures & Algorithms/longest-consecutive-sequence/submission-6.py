class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        for i, num in enumerate(nums):
            d[num] = i
        
        minR = 0
        for i in range(len(nums)):
            res = 1
            t = nums[i]
            while t+1 in d:
                t += 1
                res += 1
            minR = max(minR, res)
        
        return minR 


        
        
               
            
        
        