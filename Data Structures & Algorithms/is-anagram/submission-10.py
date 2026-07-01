class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapS, mapT = {}, {}
        for c in s:
            if c in mapS:
                mapS[c] += 1
                continue
            mapS[c] = 1
        for c in t:
            if c in mapT:
                mapT[c] += 1
                continue
            mapT[c] = 1
        return mapT == mapS
        
            

        