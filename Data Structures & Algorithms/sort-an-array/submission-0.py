class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res = []
        heapq.heapify(nums)
        while nums:
            smallest = heapq.heappop(nums)
            res.append(smallest)
        nums = res
        return nums