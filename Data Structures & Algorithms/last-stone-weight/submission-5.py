class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            max1 = stones[len(stones)-1]
            max2 = stones[len(stones)-2]
            if max2 == max1:
                del stones[len(stones)-2]
                del stones[(len(stones)-1)]
            else:
                stones[len(stones)-1] = max1 - max2
                del stones[len(stones)-2]
        if len(stones) == 0:
            return 0
        return stones[0]
        