class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            l = 0
            r = len(nums)-1
            leftOut = 1
            rightOut = 1
            while l < i:
                leftOut = leftOut * nums[l]
                l+=1
            while r > i:
                rightOut = rightOut * nums[r]
                r-=1
            res.append(leftOut * rightOut)
        return res
        