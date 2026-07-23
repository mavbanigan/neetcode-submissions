class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        custom_heap = []
        for num in arr:
            heapq.heappush(custom_heap, (abs(x - num), num))
        i = 0
        while i < k:
            first, second = heapq.heappop(custom_heap)
            res.append(second)
            i+=1
        return sorted(res)