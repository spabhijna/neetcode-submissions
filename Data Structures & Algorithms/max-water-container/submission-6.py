class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        mArea = 0
        while l < r:
            h_l, h_r = heights[l], heights[r]
            area = (r - l) * min(h_l,h_r)
            mArea = max(mArea, area)
            
            if h_l <= h_r:
                while l < r and heights[l] <= h_l:
                    l += 1
            else:
                while l < r and heights[r] <= h_r:
                    r -= 1
        
        return mArea
        