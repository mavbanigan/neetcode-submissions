class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_count = 0
        while l < r:
            count = (r-l) * min(heights[l], heights[r])
            if count > max_count:
                max_count = count
            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        return max_count
        