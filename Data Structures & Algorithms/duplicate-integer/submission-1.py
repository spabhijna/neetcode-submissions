class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = {}
        for num in nums:
            c[num] = c.get(num,0) + 1
        
        for v in c.values():
            if v > 1:
                return True
        
        return False
        