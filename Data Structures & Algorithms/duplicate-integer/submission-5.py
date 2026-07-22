class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapN = {}
        for i, num in enumerate(nums):
            if num in mapN:
                return True
            mapN[num] = i
        return False
        