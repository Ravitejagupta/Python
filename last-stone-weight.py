
import bisect

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        while True:
            if len(stones) <= 1:
                return stones[0]
            if stones[-1] >= sum(stones[:-1]):
                return stones[-1] - sum(stones[:-1])
            else:
                max1 = stones[-1]
                max2 = stones[-2]
                stones = stones[:-2]
                bisect.insort(stones, max1 - max2)
