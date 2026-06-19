class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} # Hashmap
        difference = 0

        for i, num in enumerate(nums):
            difference = target - num

            if difference in map and map[difference] != i:
                return [map[difference], i] 

            map[num] = i

        