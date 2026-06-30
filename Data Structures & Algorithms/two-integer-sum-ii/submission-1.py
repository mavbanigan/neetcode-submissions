class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = 0
        mapN = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in mapN:
                return [mapN[diff]+1, i+1]
            mapN[num] = i