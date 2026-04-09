class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - k

        while l < r:
            m = (l + r) // 2
            if abs(x - arr[m]) > abs(x - arr[m + k]):
                l = m + 1
            else:
                r = m
        
        return arr[l:l+k]
            

            
            



        