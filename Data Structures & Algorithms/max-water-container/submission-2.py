class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # A = lw, so
        # l = index of bar2 - index of bar1
        # w = min(bar1, bar2)
        area = 0
        max_area = 0
        l = 0
        r = len(heights)-1
        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            if area > max_area:
                max_area = area
            if heights[l] < heights[r]:
                l+=1
            elif heights[r] < heights[l]:
                r-=1
            else:
                l+=1
                r-=1
            
        return max_area

        