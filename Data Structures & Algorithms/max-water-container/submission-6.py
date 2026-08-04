class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_count = 0
        while l < r:
            count = min(heights[l], heights[r]) * (r-l)
            if count > max_count:
                max_count = count
            if heights[r] < heights[l]:
                r-=1
            else:
                l+=1
        return max_count