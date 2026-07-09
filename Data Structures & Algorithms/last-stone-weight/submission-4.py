class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            maxS1 = stones[-1]
            maxS2 = stones[-2]
            if maxS1 == maxS2:
                del stones[-1]
                del stones[-1]
            else:
                maxS1 = maxS1 - maxS2
                stones[-1] = maxS1
                del stones[-2]
        return stones[0] if stones else 0

        