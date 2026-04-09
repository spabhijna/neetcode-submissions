class Solution:
    def trap(self, height: List[int]) -> int:
        max_l, max_r = [0] * len(height), [0] * len(height)

        c_l, c_r = 0, 0
        for i in range(len(height)):
            max_l[i] = c_l
            c_l = max(c_l, height[i])
        
        for i in range(len(height)-1, -1, -1):
            max_r[i] = c_r
            c_r = max(c_r, height[i])
        
        r = 0
        for i in range(len(height)):
            s = min(max_l[i], max_r[i]) - height[i]
            r = r + s if s>=0 else r
        return r




        