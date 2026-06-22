class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = 0
        map = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in map:
                return [map[difference], i]
            map[num] = i
        

        