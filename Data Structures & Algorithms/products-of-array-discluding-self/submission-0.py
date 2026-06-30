class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute force method. O(n^2) time complexity. Does not meet requirements.
        result = [1] * len(nums)
        mapN = {}
        for d, num in enumerate(nums):
            mapN[d] = num
        i=0
        j=0
        while j < len(nums):
            if i < len(nums):
                if j != i:
                    result[j] = result[j] * mapN[i]
                i+=1
            else:
                i = 0
                j+=1
        return result

        
