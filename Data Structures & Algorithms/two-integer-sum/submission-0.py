class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        d = {}
        for i,num in enumerate(nums):
            d[target-num]=i
        
        for i,num in enumerate(nums):
            if num in d and d[num] != i:
                return [i, d[num]]


        