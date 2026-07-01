class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapS={}
        mapT={}
        for c in s:
            if c in mapS:
                continue
            mapS[c] = s.count(c)
        for c in t:
            if c in mapT:
                continue
            mapT[c] = t.count(c)
        return mapS == mapT
        