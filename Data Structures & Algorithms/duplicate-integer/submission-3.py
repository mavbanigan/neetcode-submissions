class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapNums = {}
        for i, num in enumerate(nums):
            if num in mapNums:
                return True
            mapNums[num] = i
        return False
        