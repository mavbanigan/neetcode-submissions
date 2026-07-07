class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        # A = lw
        # l = min(r, l)
        # w = r - l
        max_area = 0
        while l < r:
            area = (r-l) * min(heights[r], heights[l])
            max_area = max(area, max_area)
            if heights[r] < heights[l]:
                r-=1
            else:
                l+=1
        return max_area
        