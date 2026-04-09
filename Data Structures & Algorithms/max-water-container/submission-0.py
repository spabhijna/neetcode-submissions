class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        mArea = 0
        while l <= r:
            area = (r - l) * min(heights[l],heights[r])
            mArea = max(mArea, area)
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
        
        return mArea
        