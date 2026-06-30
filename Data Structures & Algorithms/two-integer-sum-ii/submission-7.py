class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        temp = 0
        l = 0
        r = len(numbers)-1
        while l < r:
            num = numbers[l] + numbers[r]
            if target == num:
                return [l+1, r+1]
            if num < target:
                l+=1
            else:
                r-=1
            
            