class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            p1, p2 = 0, i+1
            prefix = 1
            postfix = 1
            while p1 < i:
                prefix *= nums[p1]
                p1+=1
            while p2 < len(nums):
                postfix *= nums[p2]
                p2+=1
            res.append(prefix*postfix)
        return res
            