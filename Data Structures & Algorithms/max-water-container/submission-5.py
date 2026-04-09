class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        mArea = 0
        
        while l < r:
            # Calculate current area
            h_l, h_r = heights[l], heights[r]
            h = min(h_l, h_r)
            mArea = max(mArea, (r - l) * h)
            
            # If the left side was the bottleneck
            if h_l <= h_r:
                # Skip all bars on the left that are shorter than the current h_l
                while l < r and heights[l] <= h_l:
                    l += 1
            else:
                # Skip all bars on the right that are shorter than the current h_r
                while l < r and heights[r] <= h_r:
                    r -= 1
        
        return mArea