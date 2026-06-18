class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        out = []
        for n in nums:
            if n in out:
                return True
            else:
                out.append(n)
        return False
        
        