class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result=[1] * length
        before = 1
        after = 1
        for i in range(length):
            result[i] *= before
            before *= nums[i]
        for i in range(length-1, -1, -1):
            result[i] *= after
            after *= nums[i]
        return result
        