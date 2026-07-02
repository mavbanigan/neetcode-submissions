class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        res = 0
        mapN = {}
        counter = 1
        while r < len(s):
            if s[r] in mapN:
                l = max(l, mapN[s[r]]+1)
            counter=r-l+1
            res = max(res, counter)
            mapN[s[r]] = r
            r+=1
        return res

        