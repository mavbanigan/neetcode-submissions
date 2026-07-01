class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums)
        result =[]
        for i, num in enumerate(sort):
            if num == sort[i-1] and i > 0:
                continue
            l=i+1
            r = len(sort)-1
            while l < r:
                threeSum = num + sort[l] + sort[r]
                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                else:
                    result.append([num, sort[l], sort[r]])  
                    l+=1
                    while sort[l] == sort[l-1] and l < r:
                        l+=1
        return result

        