class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        while i < len(nums):
            if j < len(nums)-1 and i==j:
                j+=1
            if nums[i]+nums[j]==target:
                return [i, j]
            elif j == len(nums)-1:
                j = 1
                i+=1
            else:
                j+=1
        return [0, 0]

        