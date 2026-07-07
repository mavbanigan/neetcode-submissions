class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # We need an algorithm that checks for repeating characters,
        # but it allows for k characters that can be replaced.
        # If that k limit is reached and overpassed,
        # we need to reset to the last known character, and reset the k counter
        mapS = {}
        res = 0
        l = 0
        for r in range(len(s)):
            mapS[s[r]] = mapS.get(s[r], 0) + 1
            while (r - l + 1) - max(mapS.values()) > k:
                mapS[s[l]] -= 1
                l+=1
            res = max(res, r - l + 1)
        return res

            
